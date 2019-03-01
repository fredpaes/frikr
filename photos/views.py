from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.
def home(request):
    photos = Photo.objects.filter(visibility='PUB').order_by('-created_at')
    context = {'list': photos}
    return render(request, 'photos/home.html', context)

def detail(request, id):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param id: id de la foto
    :return: HttpResponse
    """
    """
    try:
        info = Photo.objects.get(pk=id)
    except Photo.DoesNotExist:
        info = None
    except Photo.MultipleObjects:
        photo = None
    """
    possible_info = Photo.objects.filter(pk=id)
    info = possible_info[0] if len(possible_info) == 1 else None
    if info is not None:
        context = {'photo': info}
        return render(request, 'photos/detail.html', context)
    else:
        # return HttpResponse('404 papu')
        return HttpResponseNotFound('No existe la foto')