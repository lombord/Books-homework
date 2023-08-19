from django import template

register = template.Library()


@register.filter
def get_url(obj, name=None):
    return obj.get_absolute_url(**{'name': name} if name else {})
