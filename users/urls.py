from django.urls import path
from .views import *

urlpatterns = [
    path('in', log_in, name='login'),
    path('out', log_out, name='logout'),
]