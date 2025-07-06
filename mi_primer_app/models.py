from django.db import models

class Repuesto(models.Model):
    num_parte = models.CharField(max_length=10)
    descripcion = models.TextField(blank=True, null=True)
    importe = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.num_parte

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Unidad(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
