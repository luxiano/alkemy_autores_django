from django.urls import path
from .views import (
    # AutorListAPIView,
    # AutorRetrieveAPIView,
    AutoresFrasesListRetrieveAPIView,
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
    # Pero también le damos su ruta propia
    path('autores/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'autor'}, name='api_listar'),
    path('autores/<int:pk>/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'autor'}, name='api_detalle'),
    path('autores/<int:pk>/frases/', AutoresFrasesListRetrieveAPIView.as_view(),
         {'model': 'autor_frases'}, name='api_autor_frases'),
    # Frases
    path('frases/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'frases'}, name='api_listar'),
    path('frases/<int:pk>/', AutoresFrasesListRetrieveAPIView.as_view(), 
         {'model': 'frases'}, name='api_detalle'),
]