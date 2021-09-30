from django.db import models

class TipoLicor(models.Model):
    nombre = models.CharField(max_length=100)
    #foto = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    def numProductos(self):
        pass
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoLicor, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.TextField()
    #foto = models.ImageField(blank=True, null=True)
    calificacion = models.FloatField(default=0)
    
    @property
    def tipoE1(self):
        from Productos.serializers import TipoSerial
        return TipoSerial(self.tipo).data
    
    def __str__(self):
        return self.nombre
    
    @property
    def calcularCalificacion(self):
        comentarios = self.comentarios_set.all()
        calificacion = 0
        for comentario in comentarios:
            calificacion += comentario.calificacion
        return calificacion/len(comentarios)
    
class Comentario(models.Model):
    usuario = models.CharField(max_length=200)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    
    def __str__(self):
        return self.usuario + " - " + self.producto.nombre
    
     
    
    
    
