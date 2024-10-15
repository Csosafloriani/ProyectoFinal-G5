from django.contrib import admin

from .models import Categoria, Noticia, Denuncia

class  CategoriaAdmin(admin.ModelAdmin):
    list_display=['nombre']
    search_fields = ['nombre']

class NoticiaAdmin(admin.ModelAdmin):
    list_display=['titulo', 'autor', 'cuerpo', 'imagen', 'categoria_noticia', 'fecha']
    search_fields=['titulo',]

class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('noticia', 'usuario', 'motivo', 'fecha')  
    list_filter = ('motivo', 'fecha')  
    search_fields = ('usuario__username', 'noticia__titulo')  


admin.site.register(Denuncia, DenunciaAdmin)
admin.site.register(Categoria, CategoriaAdmin)#puse en el admin
admin.site.register(Noticia, NoticiaAdmin)#puse en el admin
