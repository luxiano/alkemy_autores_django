#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializers import AutorSerializer, FrasesSerializer
from autores.models import Autor
from frases.models import Frases

# Create your views here.

# Vista general para todos los métodos HTTP
# Por el bien de aprender paso a paso, dejaré separadas las vistas
# de Autores y Frases, aunque podrían ser unidas en una sola vista
# y con un if cambiar el queryset.

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class FrasesViewSet(viewsets.ModelViewSet):
    serializer_class = FrasesSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]

    def get_queryset(self):
        if self.kwargs.get('model') == 'autor_frases':
            autor_id = self.kwargs.get('pk')
            return Frases.objects.filter(autor=autor_id)
        else:
            return Frases.objects.all()