from django.db import models
from apps.usuarios.models import Usuario

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

    #autor = models.ForeignKey('auth.user',  on_delete=models.CASCADE)
	titulo = models.CharField(max_length = 150)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'noticias')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
   

	def __str__(self):
		return self.titulo

class Comentario(models.Model):

    noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    texto = models.TextField(max_length = 1500)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	    return f"{noticia}->{texto}"