from django.test import TestCase, Client

from posts.models import Post, User, Group


class PostGroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        User.objects.create_user(username='test')
        Group.objects.create(title='test', description='test')
        cls.group = Group.objects.get(title='test')
        cls.post = Post.objects.create(
            text='This is the first post',
            author=User.objects.get(id=1),
            group=Group.objects.get(id=1)
        )

    def test_verbose_name(self):
        for field in self.post._meta.get_fields():
            with self.subTest(field=field):
                self.assertTrue(field.verbose_name)

    def test_str(self):
        self.assertEqual(self.post.__str__(), self.post.text[:15])
        self.assertEqual(self.group.__str__(), self.group.title)