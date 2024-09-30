from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	ROLES = (
		#('valorEnBaseDeDatos', 'RepresentacionLegible')
		('no_registrado', 'No Registrado'),
		('registrado', 'Registrado'),
		('admin', 'Administrador'),
	)
	#se utiliza para almacenar el rol del usuario
	#por defecto es 'registrado'
	rol = models.CharField(max_length=20, choices=ROLES, default='registrado') 
