from django.shortcuts import render
from django.views import View 
from .models import Tegning, Kategori 
from django.http import HttpResponse 


def index(request):
    return render(request, 'polls/base.html')
