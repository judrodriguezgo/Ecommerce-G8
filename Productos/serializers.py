# crear nuestros serializadores
# serializador -> objeto python -> diccionario -> JSON
from rest_framework import serializers
from Productos.models import *

class TipoSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoLicor
        fields = '__all__'
        # fields = ['nombre', 'foto']


