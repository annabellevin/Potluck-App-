from django.urls import path

from . import views
from . import addtodb
from django.http import HttpRequest as request

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodb', addtodb.addtodb, name='POST')
]