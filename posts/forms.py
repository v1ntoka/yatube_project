from django.forms import ModelForm

from posts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['name', 'email', 'subject', 'body']
