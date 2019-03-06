from django import forms
from django.forms import TextInput

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Nombre de usuario')
    user_password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())