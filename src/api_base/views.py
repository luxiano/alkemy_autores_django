#from django.shortcuts import render
#from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .serializers import AutorSerializer, FrasesSerializer
from autores.models import Autor
from frases.models import Frases

# Create your views here.
class AutoresFrasesListRetrieveAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin):
    #https://www.django-rest-framework.org/api-guide/generic-views/#get_querysetself
    def get_queryset(self):
        if self.kwargs.get('model') == 'autor':
            return Autor.objects.all()
        elif self.kwargs.get('model') == 'frases':
            return Frases.objects.all()
        elif self.kwargs.get('model') == 'autor_frases':
            autor_id = self.kwargs.get('pk')
            return Frases.objects.filter(autor=autor_id)
        else:
            return None

    #https://www.django-rest-framework.org/api-guide/generic-views/#get_serializer_classself
    def get_serializer_class(self):
        if self.kwargs.get('model') == 'autor':
            return AutorSerializer
        elif self.kwargs.get('model') == 'frases':
            return FrasesSerializer
        elif self.kwargs.get('model') == 'autor_frases':
            return FrasesSerializer
        else:
            return None

    #https://www.django-rest-framework.org/api-guide/views/#initialself-request-args-kwargs
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs and kwargs.get('model') != 'autor_frases':
            #https://www.django-rest-framework.org/api-guide/generic-views/?q=ListRetrieveAPIView#retrievemodelmixin
            return self.retrieve(request, *args, **kwargs)
        if 'pk' in kwargs and kwargs.get('model') == 'autor_frases':
            return self.list(request, *args, **kwargs)
        else:
            #https://www.django-rest-framework.org/api-guide/generic-views/?q=ListRetrieveAPIView#listmodelmixin
            return self.list(request, *args, **kwargs)