from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from Bookshop.api.resources import BookResource
from django.contrib.auth.views import login, logout
from . import views

v1_api = Api(api_name='v1')
v1_api.register(BookResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlineBookshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),

    # requirement
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^$', views.home, name='home'),
    url(r'^books/', include('Bookshop.urls')),
)
