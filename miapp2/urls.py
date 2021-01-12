"""urls miapp2"""

from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('', views.mostrar_index2),
    path("index/", views.index),

=======
    path("extendido/", views.mostrar_extendido),
    path("base/", views.mostrar_base),
  
>>>>>>> f09d1cc634d116a7cbf467449a925e98761bcf03
]

