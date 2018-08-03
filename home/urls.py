from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list')
]