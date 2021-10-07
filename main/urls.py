from django.urls import path
from main.views import *
from person.views import *

urlpatterns = [
    path('', Home, name='home'),
    path('person/', Index, name='index'),
 
]
