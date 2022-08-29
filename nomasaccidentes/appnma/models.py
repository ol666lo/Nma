from xml.parsers.expat import model
from django.db import models
from easygui import passwordbox

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=20)
    pswd = models.CharField(max_length=20)

    def __str__(self):
        return super.username