from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def activetabs(request, urls):
    path = request.path.split('/')[1]
    if path in (url for url in urls.split()):
        return 'active'
    return ''
