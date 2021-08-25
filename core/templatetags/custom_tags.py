from django.template import Library

from product.models import Category

register = Library()


@register.filter
def split(text, split_by=' '):
    return text.split(split_by)


@register.filter
def add_value(a, value):
    print(type(a))
    return a + value


@register.simple_tag
def get_categories(limit=None):
    return Category.objects.filter(is_published=True)[0:limit]
