
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),

	path('<int:pk>/', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
    #path ('comentario/editar/<int:id_comentario>', views.Comentario_editar, name="comentario_editar"),
    #path('comentario/delete/<int:id_comentario>', views.Comentario_delete, name='comentario_delete'),
	
    path('noticia/editar/<int:id_noticia>', views.Noticia_editar, name='editar_noticia'),
	path('cargar_noticia/', views.Noticia_form, name = 'cargar_noticia'),
	path('noticia/delete/<int:id_noticia>', views.Noticia_delete, name = 'noticia_delete'), 
	
]
    
	


