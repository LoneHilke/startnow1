from re import T
from django.contrib import admin
from .models import Kategori, Tegning

# Register your models here.
admin.site.register(Kategori)
admin.site.register(Tegning)