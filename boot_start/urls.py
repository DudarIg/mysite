from django.urls import path
from .views import *
app_name = 'boot_start'

urlpatterns = [
    path('', bootstart, name='bootstart'),
]