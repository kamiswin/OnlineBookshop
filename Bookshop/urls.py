from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<name>[^/]+)/$', views.specification, name='specification'),
)
