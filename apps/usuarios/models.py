from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	ROLES= (
		('no_registrado', 'No Registrado'),
		('registrado', 'Registrado'),
		('admin', 'Administrador'),
	)


rol = models.CharField(max_length=20, choices='ROLES', default='registrado')

