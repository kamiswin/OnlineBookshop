from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<m_isbn>[^/]+)/$', views.specification, name='specification'),
)
