from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()

    # class Meta:
    #     ordering = ("title",)
    #     verbose_name = "Group"
    #     verbose_name_plural = "Groups"
    #     unique_together = ("title", "slug")
    #     index_together = ("title", "slug")

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groups', blank=True, null=True)
