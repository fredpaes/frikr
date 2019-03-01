from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('detail/<int:id>', detail),
]