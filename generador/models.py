from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import unicodedata

class Direcciones(models.Model):
    nombre = models.CharField(max_length=200)
    prefijo = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
    
    def __str__(self):
        return self.nombre

class Contrasenas(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.ForeignKey(Direcciones, on_delete = models.PROTECT, related_name= 'dir')
    contrasena = models.CharField('Contraseña', max_length = 50, unique = True, null = True, blank = True, editable = False)
    
    class Meta:
        verbose_name = 'Contraseña'
        verbose_name_plural = 'Contraseñas'
        

@receiver(post_save, sender = Contrasenas)
def make_password(sender, instance, **kwargs):
    nombre = instance.nombres[0:2]
    apellido = instance.apellidos[0:2]
    id_contra = addCero(instance.id)
    dir_prefijo = instance.direccion.prefijo
    password = '{}{}{}{}'.format(dir_prefijo, id_contra, nombre, apellido).upper()
    cleaned_pass = unicodedata.normalize("NFKD", password).encode("ascii","ignore").decode("ascii")
    Contrasenas.objects.filter(id = instance.id).update(contrasena = cleaned_pass)
    
def addCero(num):
    if int(num) < 10:
        return '0' + str(num)
    else:
        return num