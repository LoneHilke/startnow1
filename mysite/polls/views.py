from django.shortcuts import render
from django.views import View 
from .models import Tegning, Kategori 
from django.http import HttpResponse 


def index(request):
    return HttpResponse("Hello, we are making a new app")
