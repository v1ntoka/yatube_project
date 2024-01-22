from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_page(self):
        response = self.guest_client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.guest_client.get('/about/contact/')
        self.assertEqual(response.status_code, 200)

    def test_technology_page(self):
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, 200)
