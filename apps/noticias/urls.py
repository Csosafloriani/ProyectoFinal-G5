
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
	path('agregar/', views.agregar_noticia, name='agregar'),
    path('noticia/<pk>/editar/', views.editar_noticia, name='editar'),
	path('noticia(<pk>eliminar/', views.eliminar_noticia, name='eliminar'),

    ]
	


