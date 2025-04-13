from django.urls import path
from .views import (
    FrasesListView,
    FrasesCreateView,
    FrasesUpdateView,
    FrasesDeleteView,
    frases_json,
    frases_por_autor,
)

app_name = 'frases'

urlpatterns = [
    path('', FrasesListView.as_view(), {'todas': 'todas'}, name='listado'),
    path('crear/', FrasesCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', FrasesUpdateView.as_view(), name='editar'),
    path('borrar/<int:pk>/', FrasesDeleteView.as_view(), name='borrar'),
    path('json/', frases_json, name='frases_json'),
    path('autor/<int:pk>/', frases_por_autor, name='frases_por_autor'),
    path('visibles/', FrasesListView.as_view(), {'visible': True}, name='listado_visibles'),
    path('invisibles/', FrasesListView.as_view(), {'visible': False}, name='listado_invisibles'),
]
