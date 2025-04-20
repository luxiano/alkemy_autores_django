# Aclaración sobre este archivo:
# En el proyecto de ejemplo de Artículos, todo esto está en el archivo
# urls.py del proyecto, pero en este caso lo pongo aquí para:
# 1) Separar las urls de la API del resto de la 
# aplicación (para evitar conflictos con 'frases/')
# 2) Mantener la modularidad
# Entonces, mantengo que tengo que incluir '/api/' en la url

from django.urls import path, include
# Router para API
from rest_framework import routers
from .views import AutoresViewSet, FrasesViewSet

# Crear un router y registrar el viewset
# Tuve que registar basename para quitar 'queryset = Frases.objects.all()' de 
# FrasesViewSet. Funcionaba, pero se ve mejor así
router = routers.SimpleRouter()
router.register(r'autores', AutoresViewSet, basename='autores')
router.register(r'frases', FrasesViewSet, basename='frases')

app_name = 'api_base'

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
    path('autores/<int:pk>/frases/', FrasesViewSet.as_view({'get': 'list'}),
         {'model': 'autor_frases'}, name='api_autor_frases'),
]