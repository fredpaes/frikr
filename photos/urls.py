from django.urls import path
from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('home', HomeView.as_view(), name='index'),
    path('detail/<int:id>', DetailView.as_view(), name='detalle'),
    path('new', CreateView.as_view(), name='new_photo')
]