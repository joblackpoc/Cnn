from django.urls import path
from .views import *
from person.views import *

urlpatterns = [
    path('', Home, name='home'),
    path('person/', Index, name='index'),
 
]
