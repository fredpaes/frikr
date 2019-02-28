from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    return HttpResponse('Hola mundo')

def test(request):
    return HttpResponse('es una prueba')