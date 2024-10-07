from django.contrib import admin

from .models import Categoria, Noticia,Comentario

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Comentario)