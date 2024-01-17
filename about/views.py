from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'about/contacts.html'


class TechView(TemplateView):
    template_name = 'about/tech.html'


class AboutView(TemplateView):
    template_name = 'about/about.html'
