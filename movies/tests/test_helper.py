from django.test import SimpleTestCase
from ..helper import Helper


class TestHelper(SimpleTestCase):
    """
    This class tests the Helper functions
    """

    movies_url = "https://ghibliapi.herokuapp.com/films"
    url_404 = "https://ghibliapi.herokuapp.com/404"

    def test_make_request_error(self):
        """
        Tests the a wrong api returns a error status
        """
        response = Helper.make_request(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_make_successful_call(self):
        """
        Tests the a page found returns 200
        """
        response = Helper.make_request(self.movies_url)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        movie_keys: set[str] = {'id', 'title',
                      'description', 'director',
                      'producer', 'release_date',
                      'rt_score', 'people',
                      'species', 'locations',
                      'vehicles', 'url'}
        self.assertEqual(json_data[0].keys(), movie_keys)
