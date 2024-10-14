from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import logout 
# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'


def logout_view(request):
	logout(request)
	messages.success(request, 'Has cerrado sesión correctamente.')
	return redirect('login') #lo redirige a la pantalla de login