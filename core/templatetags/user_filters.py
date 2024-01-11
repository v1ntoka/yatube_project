from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def uglify(text):
    return ''.join(w.lower() if (i % 2) else w.upper() for i, w in enumerate(text))
