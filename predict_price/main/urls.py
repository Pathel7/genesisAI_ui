from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('form_entries', views.entries_form, name='entries'),
    path('myform', views.myform, name='myform'),
    path('predict', views.predict, name='predict'),
]