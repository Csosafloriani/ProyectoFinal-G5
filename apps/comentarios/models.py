from django.db import models

from apps.usuarios.models import Usuario
from apps.noticias.models import Noticia

# Create your models here.
class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')

	def __str__(self):
		return f"{self.noticia}->{self.texto[:50]}"