from django.db import models
from django.template.defaultfilters import truncatechars
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Post's text",
        help_text="Enter text here"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date published"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Author"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        verbose_name="Group",
        help_text="Choose group",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]

    def short_text(self):
        return truncatechars(self.text, 35)
