from django.urls import path
from .views import First

urlpatterns = [
    path('', First , name='First'),

]
