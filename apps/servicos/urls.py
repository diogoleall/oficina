from django.contrib import admin
from django.urls import path, include
# from apps.usuarios import views

urlpatterns = [
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('admin/', admin.site.urls),
    path('', include('geral.urls', namespace='geral')),
]