#from django.shortcuts import render
#from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import GenericAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin
from .serializers import AutorSerializer, FrasesSerializer
from autores.models import Autor
from frases.models import Frases

# Create your views here.

# Podría hacer una clase totalmente genérica que sirviera para ambos modelos, 
# para List, Retrieve, Destroy, Create y Update, pero por la simplicidad de la 
# vista y porque el profesor pidió algo específico, lo haré de esta manera.

# Get/Retrieve y List
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
        

# Crear, actualizar y borrar para AUTORES
class AutoresCreateAPIView(CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutoresUpdateAPIView(UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutoresDestroyAPIView(DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# Crear, actualizar y borrar para FRASES
class FrasesCreateUpdateDestroyAPIView(GenericAPIView, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = Frases.objects.all()
    serializer_class = FrasesSerializer

    # Al ser la misma vista para crear, actualizar y borrar,
    # es necesario asegurarse de que el método request sea el correcto,
    # ya que si uso, por ejemplo, el método PUT para "crear/", aunque la URL
    # no sea la correcta, el método sí lo es, y se editaría el pk que se le pase
    # Esto está solamente como ejercicio, para ver alternativas
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)