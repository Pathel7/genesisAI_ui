from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('form_entries', views.index, name='entries'),
]