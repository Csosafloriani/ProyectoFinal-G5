from typing import Any 
from django.db import models
from apps.usuarios.models import Usuario

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

	titulo = models.CharField(max_length = 150)
	autor=models.ForeignKey(Usuario, on_delete = models.CASCADE, null=True)#agregue autor
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'noticias')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha_publicación = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.titulo
	def delete(self, using= None, keep_parents=False, *args, **kwargs) -> tuple[int, dict[str, int]]:
		self.imagen.delete(self.imagen.name)
		super(Noticia, self).delete(*args, **kwargs)
#borra las imagenes

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha_publicación = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.noticia , self.texto

	