from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.CharField(max_length=50, unique=True)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=120)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
