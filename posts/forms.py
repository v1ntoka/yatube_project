from django.forms import ModelForm

from posts.models import Contact, Post


class ContactForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['name', 'email', 'subject', 'body']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group', 'image']
