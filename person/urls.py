from person.views import Index
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('about/', About, name='about'),
    path('multistepformexample/', multistepformexample, name='multistepformexample'),
    path('multistepformexample_save/', multistepformexample_save, name='multistepformexample_save'),

]
