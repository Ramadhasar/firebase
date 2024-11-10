# blog/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_homepage(context):
    request = context['request']
    return request.path == '/'
