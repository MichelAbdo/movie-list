from django.test import SimpleTestCase
from django.urls import reverse
from django.core.cache import cache
from ..movies_service import MoviesService
import httpretty


class TestViews(SimpleTestCase):
    """
    This class tests the index view
    """

    def setUp(self):
        self.response = self.client.get(reverse('index'))
        self.movies = MoviesService().get_movies_people()

    def test_index_page(self):
        """
        Tests the html page used for the associated url
        Tests the page contains the word Movies
        """
        self.assertTemplateUsed(self.response, 'movies/index.html')
        self.assertContains(self.response, "Movies")

    def test_index_page_set_cache(self):
        """
        Tests that the movies are being cached
        Delete the cache, load the page, check if cache is set
        """
        cache.delete('movies_people_list')
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'movies/index.html')
        self.assertContains(response, "Movies")
        cached_movies_with_people = cache.get('movies_people_list')
        self.assertEqual(self.movies, cached_movies_with_people)

    def test_get_movies_people_get_cache_getting(self):
        """
        Tests that the movies are loaded from cache when the cache key is set
        """
        #Set the cache manually
        cache.set('movies_people_list', self.movies)
        # Stub the request to return an empty object
        httpretty.register_uri(
            httpretty.GET,
            "https://ghibliapi.herokuapp.com/films",
            body=str('[]'),
            content_type="application/json")
        httpretty.enable()
        # Load the page
        response = self.client.get(reverse('index'))
        # Check if the content is loaded
        self.assertContains(response, "Movies")
        self.assertContains(response, self.movies[0]['title'])
        httpretty.disable()

    def test_get_movies_people_cache_expiry(self):
        """
        Tests that movie people is being cached
        """
        # cache.touch('a', 10)
        # print('***************************************')
        # print(cache._expire_info.get('movies_people_list'))
        # print('***************************************')
        # cache_expire_time.seconds
