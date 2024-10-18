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
	fecha = models.DateTimeField(auto_now_add=True)
	publicado = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo
	
	def delete(self, using= None, keep_parents=False, *args, **kwargs) -> tuple[int, dict[str, int]]:
		self.imagen.delete(self.imagen.name)
		super(Noticia, self).delete(*args, **kwargs)

class Denuncia(models.Model):
    MOTIVOS_DENUNCIA = [
        ('SPAM', 'Spam'),
        ('COPYRIGHT', 'Infracción de Copyright'),
        ('OFENSIVO', 'Contenido ofensivo'),
        ('OTRO', 'Otro'),
    ]

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='denuncias')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=20, choices=MOTIVOS_DENUNCIA)
    comentario = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Denuncia de {self.usuario} sobre {self.noticia}'
