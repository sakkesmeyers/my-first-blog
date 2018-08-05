from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.maandprogrammas_list, name='maandprogrammas_list')
]