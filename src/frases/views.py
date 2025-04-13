from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers
from django.urls import reverse_lazy
from .models import Frases
from autores.models import Autor

# Create your views here.
class FrasesListView(ListView):
    template_name = 'frases/listar.html'
    context_object_name = 'listado_frases'

    def get_queryset(self):
        visible = self.kwargs.get('visible')
        if visible == True:
            queryset = Frases.objects.filter(visible=True)
        elif visible == False:
            queryset = Frases.objects.filter(visible=False)
        else:
            queryset = Frases.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["visible"] = self.kwargs.get('visible')
        context["todas"] = self.kwargs.get('todas')
        return context
    

class FrasesCreateView(CreateView):
    model = Frases
    template_name = 'editar.html'
    #fields = ['autor', 'frase', 'comentarios', 'fecha_frase', 'visible']
    fields = '__all__'
    success_url = reverse_lazy('frases:listado')
    
    # Sé que esto se puede hacer desde FormView, pero no quiero hacerlo
    # porque, si bien no vimos nada de lo que sigue en clase, me parece que
    # ya sería demasiado para lo que sí vimos. Toca repetir lo siguiente.

    def get_form(self, form_class = None): 
        #https://stackoverflow.com/a/73400841
        #https://stackoverflow.com/a/29202201
        form = super().get_form(form_class)
        form.fields['fecha_frase'].label = 'Fecha de la frase'
        form.fields['frase'].widget.attrs['rows'] = '5'
        return form
    
    #https://docs.djangoproject.com/en/5.1/ref/class-based-views/mixins-simple/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_crear"] = "Crear frase"
        return context


class FrasesUpdateView(UpdateView):
    model = Frases
    template_name = 'editar.html'
    fields = '__all__'
    success_url = reverse_lazy('frases:listado')

    def get_form(self, form_class = None): 
        form = super().get_form(form_class)
        form.fields['fecha_frase'].label = 'Fecha de la frase'
        form.fields['frase'].widget.attrs['rows'] = '5'
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_crear"] = "Modificar frase"
        return context
    
class FrasesDeleteView(DeleteView):
    model = Frases
    template_name = 'frases/borrar.html'
    success_url = reverse_lazy('frases:listado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_borrar"] = "Borrar frase"
        return context


def frases_json(request):
    frases = get_list_or_404(Frases.objects.filter(visible=True))
    frases_json = serializers.serialize('json', frases)
    #return JsonResponse(autores_json, safe=False)
    return render(request, 'json.html', {'json': frases_json, 'titulo': 'Frases'})

def frases_por_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    frases = Frases.objects.filter(autor=autor)
    return render(request, 'frases/por_autor.html', {'autor': autor, 'frases': frases})