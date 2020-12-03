from django.test import SimpleTestCase
from django.urls import reverse


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
