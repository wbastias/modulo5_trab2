"""urls miapp2"""

from django.urls import path
from . import views


urlpatterns = [
    path('miapp/', views.mostrar_index2),

]

