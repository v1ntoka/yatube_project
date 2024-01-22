from django.test import TestCase, Client

from posts.models import User, Post


class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test', email='<EMAIL>', password='<PASSWORD>')
        cls.guest_client = Client()
        cls.authorised_client = Client()
        cls.authorised_client.force_login(cls.user)
        cls.post = Post.objects.create(
            text="test text",
            author=cls.user
        )
        cls.addresses = {
            '/': (200, 200),
            '/group/': (302, 200),
            '/profile/' + str(cls.user.username): (302, 200),
            '/post/' + str(cls.post.id): (302, 200),
            '/create/': (302, 200)
        }

    def test_views(self):
        for url, expected_status in self.addresses.items():
            with self.subTest(url=url):
                self.assertEqual(self.guest_client.get(url).status_code, expected_status[0])
                self.assertEqual(self.authorised_client.get(url).status_code, expected_status[1])

    def test_edit_post(self):
        """Пост может редактировать либо его создатель, либо стафф"""
        response_guest = self.guest_client.get('/post/' + str(self.post.id) + '/edit/')
        response_authorised = self.authorised_client.get('/post/' + str(self.post.id) + '/edit/')
        another_user, staff_user = User.objects.create_user(username='another',
                                                            password='<PASSWORD>'), User.objects.create_user(
            username='staff', password='<PASSWORD>', is_staff=True)
        another_client, staff_client = Client(), Client()
        another_client.force_login(another_user)
        staff_client.force_login(staff_user)
        response_another = another_client.get('/post/' + str(self.post.id) + '/edit/')
        response_staff = staff_client.get('/post/' + str(self.post.id) + '/edit/')
        self.assertEqual(response_guest.status_code, 302)
        self.assertEqual(response_authorised.status_code, 200)
        self.assertEqual(response_another.status_code, 403)
        self.assertEqual(response_staff.status_code, 200)

    def test_nonexistent_post(self):
        response_guest = self.guest_client.get('/jopa/')
        response_authorised = self.authorised_client.get('/jopa/')
        self.assertEqual(response_guest.status_code, 404)
        self.assertEqual(response_authorised.status_code, 404)
