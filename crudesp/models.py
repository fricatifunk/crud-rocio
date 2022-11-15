from contextlib import nullcontext
from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.
class especialista(models.Model):
    id=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=100,verbose_name="nombre")
    Apellido=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='imagenes/', verbose_name="foto", null=True)
    correo=models.EmailField(verbose_name='correo', null=True)
    descripcion=models.TextField( verbose_name='descripcion', null=True)
    
  