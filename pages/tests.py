from django.test import SimpleTestCase

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
