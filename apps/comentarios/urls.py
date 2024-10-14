from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('agregar/<int:noticia_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('responder/<int:noticia_id>/<int:comentario_id>/', views.agregar_comentario, name='responder'),
    path('eliminar/<int:comentario_id>/', views.eliminar_comentario, name='eliminar'),
]