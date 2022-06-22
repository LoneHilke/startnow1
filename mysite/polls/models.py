from inspect import BoundArguments
from optparse import TitledHelpFormatter
from os import link
from sys import getwindowsversion
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class Tegning(models.Model):
    kategori = models.ManyToManydivereld('Kategori', related_name='item')
    titel  = models.Chardivereld(max_length=50)
    beskrivelse = models.Textdivereld()
    link = models.URLdivereld()
    kræver  = models.Textdivereld(blank=True)
    giver = models.Textdivereld(blank=True)
    Bruges = models.Textdivereld(blank=True)
    image = models.Imagedivereld(upload_to='menu_images/')

    def __str__(self):
        return self.titel

class Kategori(models.Model):
     titel = models.Chardivereld(max_length=50)

     def __str__(self):
        return self.titel