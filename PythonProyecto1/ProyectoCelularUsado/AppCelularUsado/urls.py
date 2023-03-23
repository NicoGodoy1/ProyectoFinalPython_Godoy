from django.urls import path
from AppCelularUsado import views


urlpatterns = [
    path('', views.inicio),
    path('celular', views.celular), 
    path('usuario', views.usuario),
    path('comentarios', views.comentarios),
]