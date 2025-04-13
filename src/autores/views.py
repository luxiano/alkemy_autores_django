from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Autor
from frases.models import Frases

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'autores/home.html')

def listado(request, inactivo=False):
    autores = None

    if inactivo:
        autores = Autor.objects.filter(activo=False)
    else:
        autores = Autor.objects.filter(activo=True)
    return render(request, 'autores/listar.html', 
                  {'autores': autores, 'inactivo': inactivo})

def listado_json(request):
    autores = get_list_or_404(Autor)
    autores_json = serializers.serialize('json', autores)
    #return JsonResponse(autores_json, safe=False)
    return render(request, 'json.html',
                  {'json': autores_json, 'titulo': 'Autores'})

def detalle_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    cantidad_frases = Frases.objects.filter(autor=autor).count()
    return render(request, 'autores/detalle.html', {'autor': autor, 'cantidad_frases': cantidad_frases})

def borrar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return HttpResponseRedirect(reverse('autores:listado'))

def cambiar_estado(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = not autor.activo
    autor.save()
    return HttpResponseRedirect(reverse('autores:listado'))


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('autores:listado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_crear"] = "Crear autor"
        return context


class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('autores:listado')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_crear"] = "Modificar autor"
        return context