from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Repuesto(models.Model):
    num_parte = models.CharField(max_length=10)
    descripcion = models.TextField(blank=True, null=True)
    importe = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.num_parte


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
