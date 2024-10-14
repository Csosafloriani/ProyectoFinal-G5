from django.contrib import admin

from .models import Categoria, Noticia

class  CategoriaAdmin(admin.ModelAdmin):
    list_display=['nombre']
    search_fields = ['nombre']

class NoticiaAdmin(admin.ModelAdmin):
    list_display=['titulo', 'autor', 'cuerpo', 'imagen', 'categoria_noticia', 'fecha_publicación']
    search_fields=['titulo',]

admin.site.register(Categoria, CategoriaAdmin)#puse en el admin
admin.site.register(Noticia, NoticiaAdmin)#puse en el admin