from django.shortcuts import render
from django.http import HttpResponse 


def index(request):
    return HttpResponse("Hello, we are making a new app")