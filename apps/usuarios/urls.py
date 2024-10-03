from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   

]