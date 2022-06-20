from inspect import BoundArguments
from optparse import TitledHelpFormatter
from os import link
from sys import getwindowsversion
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class Tegning(models.Model):
    kategori = models.ManyToManyField('Kategori', related_name='item')
    titel  = models.CharField(max_length=50)
    beskrivelse = models.TextField()
    link = models.URLField()
    kræver  = models.TextField(blank=True)
    giver = models.TextField(blank=True)
    Bruges = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.titel

class Kategori(models.Model):
     titel = models.CharField(max_length=50)

     def __str__(self):
        return self.titel