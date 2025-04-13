from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(
        max_length=30,
        choices=[
            ('ARG', 'Argentina'),
            ('BRA', 'Brasil'),
            ('CHL', 'Chile'),
            ('USA', 'Estados Unidos'),
            ('ESP', 'España'),
        ],
        default='ARG'
    )
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""{self.nombre}"""

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'