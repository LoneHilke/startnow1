from django.shortcuts import render
from django.views import View 
from .models import Tegning, Kategori 
from django.http import HttpResponse 



def index(request):
    return render(request, 'polls/base.html')

class Kategori(View):
    def get(self, request, *args, **kwargs):
        # each item form kategori
        tegning = Tegning.objects.filter(kategori__titel__contains='Perler')
        klippe = Tegning.objects.filter(kategori__titel__contains='Knipling')
        diverse = Tegning.objects.filter(kategori__titel__contains='Filt')  
        
      
        context = {
            'tegning': tegning,
            'kklippe': klippe,
            'diverse': diverse,
            
        }
        return render(request, 'polls/kategorier.html', context)
