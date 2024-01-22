from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Group, Post

User = get_user_model()


class PostModelTestTexts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Test Group',
            slug='test-slug',
            description='Test description'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Test group'
        )

    def test_model_have_correct_object_name(self):
        self.assertEqual(str(self.group), 'Test Group', 'Incorrect __str__ method for Group')
        self.assertEqual(str(self.post), 'Test group', 'Incorrect __str__ method for Post')

    def test_verbose_name(self):
        post = self.post
        field_verbose = {
            'text': 'Post\'s text',
            'pub_date': 'Date published',
            'author': 'Author',
            'group': 'Group'
        }
        for field, expected_value in field_verbose.items():
            with self.subTest(field=field):
                self.assertEqual(post._meta.get_field(field).verbose_name, expected_value)

    def test_help_text(self):
        post = self.post
        field_help = {
            'text': 'Enter your post\'s text',
            'group': 'Choose group'
        }
        for field, expected_value in field_help.items():
            with self.subTest(field=field):
                self.assertEqual(post._meta.get_field(field).help_text, expected_value)


class PostModelTestsValid(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.usr = User.objects.create_user(username='test', password='<PASSWORD>')
        cls.post = Post.objects.create(
            text="Test text",
            author=cls.usr
        )

    def test_author(self):
        self.assertEqual(self.post.author.username, self.usr.username)
