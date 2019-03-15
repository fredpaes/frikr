from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.db.models import Q
from .models import *
from .forms import *


class PhotosQuerySet(object):
    def get_photos_queryset(self, request):
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility='PUB')
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility='PUB'))

        return photos

# Create your views here.
class HomeView(View):
    def get(self, request):
        photos = Photo.objects.filter(visibility='PUB').order_by('-created_at')
        context = {'list': photos}
        return render(request, 'photos/home.html', context)

class DetailView(View, PhotosQuerySet):
    def get(self, request, id):
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
        possible_info = self.get_photos_queryset(request).filter(pk=id).select_related('owner')
        info = possible_info[0] if len(possible_info) == 1 else None
        if info is not None:
            context = {'photo': info}
            return render(request, 'photos/detail.html', context)
        else:
            # return HttpResponse('404 papu')
            return HttpResponseNotFound('No existe la foto')

"""
# para no emplear los decoradores en la autenticación
class OnlyAuthenticatedView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return super(OnlyAuthenticatedView, self).get(request)
        else:
"""

class CreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        """
        Muestra un formulario para crear una foto
        :param request:
        :return:
        """
        success_message = ''
        form = PhotoForm()

        context = {
            'form': form,
            'msg': success_message
        }
        return render(request, 'photos/add.html', context)

    @method_decorator(login_required)
    def post(self, request):
        success_message = ''
        """
        Crea una foto en base a la información insertada (POST)
        :param request: HttpRequest
        :return: HttpResponse
        """
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

class ListView(View, PhotosQuerySet):
    def get(self, request):
        """
        Devuelve:
        - Las fotos públicas si el usuario no está autenticado
        - Las fotos del usuario autenticado o las públicas de otros
        - Si el usuario es superadmin, todas las fotos
        :param request: HttpRequest
        :return: HttpResponse
        """
        photos = self.get_photos_queryset(request)
        context = {'photos': photos}
        return render(request, 'photos/list.html', context)