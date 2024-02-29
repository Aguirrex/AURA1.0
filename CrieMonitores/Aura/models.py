from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Sala(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.nombre
    
class Equipo(models.Model):
    sala = models.ForeignKey(Sala, null = False, on_delete=models.CASCADE)
    num_equipo = models.CharField(max_length=100, null=True,blank=True)
    habilitado = models.BooleanField(default = True,null=False,blank=False)

    def __str__(self) -> str:
        return self.sala.nombre + "-" + self.num_equipo

class Estudiante(models.Model):
    cc = models.CharField(max_length=100,null=False,blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    dependencia = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.nombre
    
class ReservaEstudiantes(models.Model):
    equipo = models.ForeignKey(Equipo, null=False, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, null=False, on_delete=models.CASCADE)
    hora_reserva = models.TimeField(auto_now=False,auto_now_add=False)



    


    



