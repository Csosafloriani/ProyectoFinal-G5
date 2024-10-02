
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),
	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
	path('crear/', views.Crear_Noticia, name='crear'),
	path('editar/', views.Editar_Noticia, name= 'editar'),
    path('eliminar/', views.Eliminar_Noticia, name='eliminar'),
	
]