from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    s = 'running localy'
    if 'LOCAL' != os.environ.get('ENV', 'HEROKU'):
        s = 'running on heroku'
    return HttpResponse('<pre>' + s + '</pre>')
# Create your views here.
