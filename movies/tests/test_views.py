from django.test import SimpleTestCase
from django.urls import reverse
from django.core.cache import cache
from ..movies_service import MoviesService


class TestViews(SimpleTestCase):
    """
    This class tests the index view
    """

    def setUp(self):
        self.response = self.client.get(reverse('index'))

    def test_index_page(self):
        """
        Tests the html page used for the associated url
        Tests the page contains the word Movies
        """
        self.assertTemplateUsed(self.response, 'movies/index.html')
        self.assertContains(self.response, "Movies")

    def test_index_page_cached_successfully(self):
        """
        Tests the context is being cached
        delete the cache, load the page, check if cache is set
        """
        cache.delete('movies_people_list')
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'movies/index.html')
        self.assertContains(response, "Movies")
        cached_movies_with_people = cache.get('movies_people_list')
        movies = MoviesService().get_movies_people()
        self.assertEqual(movies, cached_movies_with_people)

    # def test_get_movies_people_cache_getting(self):
    #     """
    #     Tests that movie people is being cached
    #     """

    # def test_get_movies_people_cache_expiry(self):
    #     """
    #     Tests that movie people is being cached
    #     """
    #     # cache.touch('a', 10)
