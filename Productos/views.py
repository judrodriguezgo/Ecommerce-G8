from rest_framework import viewsets
from rest_framework.serializers import SerializerMetaclass
from Productos.serializers import *

class TipoApi (viewsets.ModelViewSet):
    serializer_class = TipoSerial
    # queryset => objetos que queremos enviar al frontend
    queryset = TipoLicor.objects.all()
    
