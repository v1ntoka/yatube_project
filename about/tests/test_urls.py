from django.test import TestCase, Client


class StaticTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about_view.html')
        # print(self._get_template_used(response, '', '', ''))
