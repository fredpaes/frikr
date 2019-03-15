from django.urls import path
from .views import *

urlpatterns = [
    path('in', LoginView.as_view(), name='login'),
    path('out', LogoutView.as_view(), name='logout'),
]