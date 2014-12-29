from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import os

def specification(request, name):
    return render(request, 'specification.html', {'book_name': name, 'book_cover_name': name, 'book_description': name})

@login_required
def show_login(request):
    return HttpResponseRedirect('/')
