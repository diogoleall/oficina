from django.urls import path

app_name = 'servicos'

from . import views 


urlpatterns = [
    path('novo/', views.novo_servico, name='novo_servico'),
    path('atualizar/int:pk>/', views.atualziar_servico, name='atualizar_servico'),
    path('ordens-servicos/int:pk>/', views.lista_ordem_servico, name='lista_ordem_servico'),
    path('criar-ordem-servico/int:pk>/', views.criar_ordem_servico, name='criar_orden_servico'),
    path('', views.lista_servico, name='lista_servicos'),
]