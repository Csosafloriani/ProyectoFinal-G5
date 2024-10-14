from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Usuario
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import logout 
# Create your views here.

#class Registro(CreateView):
#	#FORMULARIO DJANGO
#	form_class = RegistroForm
#	success_url = reverse_lazy('login')
#	template_name = 'usuarios/registro.html'

def register_view(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST) #formulario de creacion de usuario
		if form.is_valid():
			user = form.save()
			#Asignar rol por defecto
			user.rol = 'registrado'
			user.save()
			messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
			return redirect('login') #lo redirige a la pagina login
	
	else:
		form = RegistroForm()
	return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home') #lo redirige al home
		else:
			messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
	return render(request, 'usuarios/login.html')

def logout_view(request):
	logout(request)
	messages.success(request, 'Has cerrado sesión correctamente.')
	return redirect('login') #lo redirige a la pantalla de login