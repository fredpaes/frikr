from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth import logout, authenticate, login
from .forms import *

# Create your views here.
def log_in(request):
    error_messages = []
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                # username = request.POST.get('user_name', '')
                # al usar .get() indicas el valor por default al no encontrar esa clave en el diccionario
                # password = request.POST.get('user_password')
                username = form.cleaned_data.get('user_name')
                password = form.cleaned_data.get('user_password')

                user = authenticate(username=username, password=password)
                if user is None:
                    error_messages.append('Nombre de usuario o contraseña incorrecta.')
                elif user.is_active:
                    login(request, user)
                    url = request.GET.get('next', 'index')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        else:
            form = LoginForm()

        context = {
            'errors': error_messages,
            'login_form': form
        }

        return render(request, 'users/login.html', context)
    else:
        return HttpResponseNotFound('No existe el link')

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')