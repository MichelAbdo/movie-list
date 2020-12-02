from django.core.cache import cache
from .helper import Helper

class MoviesService:
    # define env variables
    movies_url = "https://ghibliapi.herokuapp.com/films"
    people_url = "https://ghibliapi.herokuapp.com/people"
    url_not_found = "https://ghibliapi.herokuapp.com/404"

    movies = []
    # _helper = Helper()

    def __init__(self):
        self._helper = Helper()

    def get_movies(self) -> list:
        self.movies = self._helper.make_request(self.movies_url)
        return self.movies

    def get_people(self) -> list:
        self.people = self._helper.make_request(self.people_url)
        return self.people

    def map_people_to_movies(self) -> list:
        # get people per movie and fill them in a dict having the movie id as key
        movie_people = {}
        for person in self.people:
            for movie in person['films']:
                movie_id = movie.rsplit('/', 1)[-1]
                if movie_id in movie_people:
                    movie_people[movie_id].append(person)
                else:
                    movie_people[movie_id] = [person]

        # for each movie, set its people
        for movie in self.movies:
            movie_id = movie.get('id')
            if movie_id in movie_people:
                movie['people'] = movie_people[movie_id]
            else:
                movie['people'] = []

        return self.movies

    def get_movies_people(self) -> list:
        movies_with_people = cache.get('movies_with_people')
        if movies_with_people is None:
            self.get_movies()
            self.get_people()
            movies_with_people = self.map_people_to_movies()
            # use cache versioning instead of expiry
            # https://docs.djangoproject.com/en/3.1/topics/cache/#cache-versioning
            # Schedule task to update cache
            # https://codeinthehole.com/projects/cacheback-asynchronous-cache-refreshing-for-django/
            # https://django.cowhite.com/blog/scheduling-taks-in-django/
            cache.set('movies_with_people', movies_with_people, 60)

        return movies_with_people
