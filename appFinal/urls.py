from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/buscar', views.buscar, name="buscar"),
    path('/acercade', views.acercade, name="acercade"),
]
