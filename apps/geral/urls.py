from django.urls import path
from . import views


app_name = 'geral'


urlpatterns = [
    path('nova-oficina/', views.nova_oficina, name='nova_oficina'),
    path('oficinas/', views.lista_oficina, name='lista_oficina'),
    path('excluir-oficina/<int:pk>/', views.excluir_oficina, name='excluir_oficina'),
    path('editar-oficina/<int:pk>/', views.editar_oficina, name='editar_oficina'),
    
    path('nova-oficina/', views.nova_oficina, name='nova_oficina'),
    path('oficinas/', views.lista_oficina, name='lista_oficina'),
    path('excluir-oficina/<int:pk>/', views.excluir_oficina, name='excluir_oficina'),
    path('editar-oficina/<int:pk>/', views.editar_oficina, name='editar_oficina'),
]