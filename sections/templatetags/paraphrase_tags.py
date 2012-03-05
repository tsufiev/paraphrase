from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='baselink')
@stringfilter
def baselink(url):
    def not_empty(str): return str != ''
    return filter(not_empty, url.split('?')[0].split('/'))[-1]
