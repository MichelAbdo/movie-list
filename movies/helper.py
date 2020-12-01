import requests
from requests.exceptions import HTTPError

class Helper:

    #define env variables
    movies_url = "https://ghibliapi.herokuapp.com/films"
    people_url = "https://ghibliapi.herokuapp.com/people"
    url_not_found = "https://ghibliapi.herokuapp.com/404"

    movies = []

    def make_request(self, url,
                     method='GET', query_params=None,
                     body=None) -> list:
        """
        @todo document all methods
        @type body: object
        """
        try:
            response = requests.request(
                method,
                url,
                params=query_params,
                json=body)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return "An HTTP error occurred"
        except Exception as err:
            print(f'Other error occurred: {err}')
            return "An Error occurred"

    def get_movies(self) -> list:
        self.movies = self.make_request(self.movies_url)
        return self.movies

    def get_people(self) -> list:
        self.people = self.make_request(self.people_url)
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
        self.get_movies()
        self.get_people()
        return self.map_people_to_movies()
