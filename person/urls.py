from person.views import Index
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('about/', About, name='about'),
]
