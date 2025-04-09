from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Autor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listado(request, inactivo=False):
    autores = None

    if inactivo:
        autores = Autor.objects.filter(activo=False)
    else:
        autores = Autor.objects.filter(activo=True)
    return render(request, 'vistas/listar.html', 
                  {'autores': autores, 'inactivo': inactivo})

def listado_json(request):
    autores = get_list_or_404(Autor)
    autores_json = serializers.serialize('json', autores)
    #return JsonResponse(autores_json, safe=False)
    return render(request, 'vistas/listado_json.html',
                  {'autores': autores_json})

def detalle_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'vistas/detalle_autor.html', {'autor': autor})

def borrar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return HttpResponseRedirect(reverse('app:listado'))

def cambiar_estado(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = not autor.activo
    autor.save()
    return HttpResponseRedirect(reverse('app:listado'))