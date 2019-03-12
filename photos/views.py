from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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
    possible_info = Photo.objects.filter(pk=id).select_related('owner')
    info = possible_info[0] if len(possible_info) == 1 else None
    if info is not None:
        context = {'photo': info}
        return render(request, 'photos/detail.html', context)
    else:
        # return HttpResponse('404 papu')
        return HttpResponseNotFound('No existe la foto')

@login_required
def create(request):
    success_message = ''
    """
    Muestra un formulario para crear una foto (POST)
    :param request: HttpRequest
    :return: HttpResponse
    """
    if request.method == 'GET':
        form = PhotoForm()
    else:
        photo_owner = Photo()
        photo_owner.owner = request.user
        form = PhotoForm(request.POST, instance=photo_owner)
        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm()
            success_message = 'Guardado con éxito '
            success_message += '<a href="' + reverse('detalle', args=[new_photo.pk]) + '">'
            success_message += 'Ver foto</a>'
    context = {
        'form': form,
        'msg': success_message
    }
    return render(request, 'photos/add.html', context)