from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Post's text",
        help_text="Enter your post's text"
    )
    pub_date = models.DateTimeField(
        verbose_name="Date published",
        auto_now_add=True,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='posts', blank=True, null=True,
                              verbose_name="Group", help_text="Choose group")

    image = models.ImageField(upload_to='posts/', verbose_name="Image", blank=True, null=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    is_answered = models.BooleanField(default=False)
