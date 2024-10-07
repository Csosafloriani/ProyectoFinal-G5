from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .models import Rol



class Usuario(AbstractUser):
	ROLES= models.ForeignKey('Rol', on_delete=models.CASCADE)(
		('no_registrado', 'No Registrado'),
		('registrado', 'Registrado'),
		('admin', 'Administrador'),
	)


class Rol(models.Model):
	nombre=models.CharField(max_length=255)
	descripcion=models.TextField()

	def __str__(self):
		return self.nombre

class Permiso(models.Model):
	nombre= models.CharField(max_length=255)
	descripción=models.TextField()

	def __str__(self):
		return self.nombre
	
class UsuarioRol(models.Model):
	usuario= models.ForeignKey(User, on_delete=models.CASCADE)
	rol=models.ForeignKey(Rol, on_delete=models.CASCADE)
     
	def __str__(self):
		return f"{self.usuario.username}
	{self.rol.nombre}"
  

