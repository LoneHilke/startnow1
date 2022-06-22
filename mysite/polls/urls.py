from urllib.parse import urlparse
from django.urls import path 
from . import views 
from .views import Index, Kategori

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('kategori/', Kategori.as_view(), name='kategori'),
]