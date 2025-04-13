from django.db import models
from autores.models import Autor

# Create your models here.
class Frases(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    frase = models.TextField()
    comentarios = models.CharField(max_length=100, blank=True)
    fecha_frase = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"""{self.frase}."""
    
    class Meta:
        verbose_name = 'Frase'
        verbose_name_plural = 'Frases'