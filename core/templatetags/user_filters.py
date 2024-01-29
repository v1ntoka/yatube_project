from django import template
from django.forms import BoundField
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
# @stringfilter
def add_class(field: BoundField, css):
    return field.as_widget(attrs={'class': css})


@register.filter
# @stringfilter
def add_placeholder(field: BoundField, placeholder):
    attrs = {'placeholder': placeholder}
    if field.field.widget.attrs:
        attrs.update(field.field.widget.attrs)
    return field.as_widget(attrs=attrs)
