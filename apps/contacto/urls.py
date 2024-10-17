from django.urls import path
from . import views


app_name = 'contacto'

urlpatterns = [
	
	path('contacto/', views.ContactoUsuario.as_view(), name = 'contacto'),    

]