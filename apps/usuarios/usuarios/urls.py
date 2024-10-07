from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),
    path('asignar-rol/<pk>/', views.asignar_rol, name='asignar_rol')

    #path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]




   