from django.test import SimpleTestCase
from django.core.cache import cache
from ..movies_service import MoviesService
from ..people_service import PeopleService


class TestMoviesService(SimpleTestCase):
    """
    This class tests the Movies Service Class functions
    """

    def setUp(self):
        self.movies = MoviesService().get_movies()

    def test_get_movies(self):
        """
        Tests that get_movies returns a valid Movie object
        """
        # movies = MoviesService().get_movies()
        movie_keys: set[str] = {'id', 'title',
                                'description', 'director',
                                'producer', 'release_date',
                                'rt_score', 'people',
                                'species', 'locations',
                                'vehicles', 'url'}
        self.assertEqual(self.movies[0].keys(), movie_keys)

    def test_map_people_to_movies(self):
        """
        Tests that map_people_to_movies returns a valid Movie object
        with a valid people object in it
        """
        people = PeopleService().get_people()
        movies = MoviesService().map_people_to_movies(self.movies, people)
        movie_keys: set[str] = {'id', 'title',
                                'description', 'director',
                                'producer', 'release_date',
                                'rt_score', 'people',
                                'species', 'locations',
                                'vehicles', 'url'}
        people_keys: set[str] = {'id', 'name',
                                 'gender', 'age',
                                 'eye_color', 'hair_color',
                                 'films', 'species', 'url'}
        people_object_is_valid: bool = False

        self.assertEqual(movies[0].keys(), movie_keys)

        for movie in movies:
            if len(movie['people']) > 0:
                people_object_is_valid = True
                self.assertEqual(movie['people'][0].keys(), people_keys)
                break

        self.assertEqual(people_object_is_valid, True)

    def test_get_movies_people_cache_setting(self):
        """
        Tests that movie people is being cached
        """
        # clear cache
        cache.delete('movies_with_people')
        movies = MoviesService().get_movies_people()
        cached_movies_with_people = cache.get('movies_with_people')
        self.assertEqual(movies, cached_movies_with_people)

    def test_get_movies_people_cache_getting(self):
        """
        Tests that movie people is being cached
        """
        # clear cache
        # cache.delete('movies_with_people')
        # movies = MoviesService().get_movies_people()
        # cached_movies_with_people = cache.get('movies_with_people')
        # self.assertEqual(movies, cached_movies_with_people)

    def test_get_movies_people_cache_expiry(self):
        """
        Tests that movie people is being cached
        """
        # cache.touch('a', 10)
        # movies = MoviesService().get_movies_people()
        # cached_movies_with_people = cache.get('movies_with_people')
        # self.assertEqual(movies, cached_movies_with_people)
