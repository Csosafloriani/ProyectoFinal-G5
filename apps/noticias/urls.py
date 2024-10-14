
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),
	path('<int:pk>/', views.Detalle_Noticias, name = 'detalle'),
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
	path('crear/', views.Crear_Noticia, name='crear'),
	path('<int:pk>/editar/', views.Editar_Noticia, name= 'editar'),
    path('<int:pk>/eliminar/', views.Eliminar_Noticia, name='eliminar'),
    
	path('cargar_noticia/', views.Noticia_form, name = 'cargar_noticia'), #agrege
    
	path('noticia/delete/<int:id_noticia>', views.Noticia_delete, name = 'noticia_delete'), #agrege
	
]