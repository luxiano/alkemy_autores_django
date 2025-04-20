from django.urls import path
from .views import (
    # AutorListAPIView,
    # AutorRetrieveAPIView,
    AutoresFrasesListRetrieveAPIView,
    AutoresCreateAPIView,
    AutoresUpdateAPIView,
    AutoresDestroyAPIView,
    FrasesCreateUpdateDestroyAPIView,
)

app_name = 'api_base'

urlpatterns = [
    # Hacemos default a la vista de listar autores, desde la raíz
    path('', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'autor'}, name='api_listar'),
    path('<int:pk>/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'autor'}, name='api_detalle'),
    path('<int:pk>/frases/', AutoresFrasesListRetrieveAPIView.as_view(),
         {'model': 'autor_frases'}, name='api_autor_frases'),
    # Crear, actualizar y borrar autores
    path('crear/', AutoresCreateAPIView.as_view(), name='api_crear'),
    path('editar/<int:pk>/', AutoresUpdateAPIView.as_view(), name='api_editar'),
    path('borrar/<int:pk>/', AutoresDestroyAPIView.as_view(), name='api_borrar'),
    # Pero también le damos su ruta propia
    path('autores/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'autor'}, name='api_listar'),
    path('autores/<int:pk>/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'autor'}, name='api_detalle'),
    path('autores/<int:pk>/frases/', AutoresFrasesListRetrieveAPIView.as_view(),
         {'model': 'autor_frases'}, name='api_autor_frases'),
    path('autores/crear/', AutoresCreateAPIView.as_view(), name='api_crear'),
    path('autores/editar/<int:pk>/', AutoresUpdateAPIView.as_view(), name='api_editar'),
    path('autores/borrar/<int:pk>/', AutoresDestroyAPIView.as_view(), name='api_borrar'),
    # Frases
    path('frases/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'frases'}, name='api_listar'),
    path('frases/<int:pk>/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'frases'}, name='api_detalle'),
    # Crear, actualizar y borrar frases
    path('frases/crear/', FrasesCreateUpdateDestroyAPIView.as_view(), name='api_crear'),
    path('frases/editar/<int:pk>/', FrasesCreateUpdateDestroyAPIView.as_view(), name='api_editar'),
    path('frases/borrar/<int:pk>/', FrasesCreateUpdateDestroyAPIView.as_view(), name='api_borrar'),
]