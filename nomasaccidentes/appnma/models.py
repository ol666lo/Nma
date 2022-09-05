from typing_extensions import runtime
from xml.parsers.expat import model
from django.db import models
from easygui import passwordbox

# Create your models here.
class VistaClientes(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    gerente = models.CharField(max_length=50)
    profesional= models.CharField(max_length=50)
    mail = models.CharField(max_length=30)
    telefono = models.IntegerField()
    dirreccion = models.CharField(max_length=50)
    visitaprimaria = models.DateTimeField()
    visitasecundaria = models.DateTimeField()
    capacitacion = models.CharField(max_length=120)
    capacitacionfecha = models.DateTimeField()
    asesoria = models.CharField(max_length=50)
    asesoriafecha = models.DateTimeField()
    actividadmejora = models.CharField(max_length=120)
    accidentabilidad = models.IntegerField()
    def __str__(self):
        return self.rut 