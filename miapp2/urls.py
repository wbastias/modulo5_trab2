from django.urls import path
from . import views

#app_name = "miapp2"

urlpatterns = [
    path("index/", views.index),
]