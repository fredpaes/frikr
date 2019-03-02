from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('detail/<int:id>', detail, name='detalle'),
]