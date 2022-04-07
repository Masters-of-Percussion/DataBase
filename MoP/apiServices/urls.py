from sys import path_hooks
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('instrument_stats', views.instrument_stats, name='instrument_stats'),
]