from rest_framework.serializers import ModelSerializer
from autores.models import Autor
from frases.models import Frases

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class FrasesSerializer(ModelSerializer):
    class Meta:
        model = Frases
        fields = '__all__'