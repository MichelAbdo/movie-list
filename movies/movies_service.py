from .helper import Helper
from .people_service import PeopleService


class MoviesService:
    """
    Class Containing Movie related functions
    """

    # @todo: Define env variables
    movies_url = "https://ghibliapi.herokuapp.com/films"
    people: list
    movies: list
    people_service: None

    def __init__(self):
        """
        Class constructor
        """
        self.people_service = PeopleService()

    def get_movies(self) -> list:
        """
        Get movies through an api call
        @return: list
        @rtype: list
        """
        self.movies = Helper.make_request(self.movies_url).json()
        return self.movies

    def get_movies_people(self) -> list:
        """
        Return movies with their people.
        For each movie add its related people
        :return: list of movies with their people
        @rtype: list
        """
        movies = self.get_movies()
        people = self.people_service.get_people()
        # Get people per movie and fill them in a dict having the movie id as key
        movie_people = {}
        for person in people:
            for movie in person['films']:
                movie_id = movie.rsplit('/', 1)[-1]
                if movie_id in movie_people:
                    movie_people[movie_id].append(person)
                else:
                    movie_people[movie_id] = [person]

        # For each movie, set its people
        for movie in movies:
            movie_id = movie.get('id')
            if movie_id in movie_people:
                movie['people'] = movie_people[movie_id]
            else:
                movie['people'] = []

        return movies
