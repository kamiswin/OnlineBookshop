from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import os

def home(request):
    return render(request, 'index.html')

@login_required
def show_login(request):
    return HttpResponseRedirect('/')
