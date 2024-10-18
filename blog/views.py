from django.shortcuts import render

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	return render(request, 't_home.html')


def Nosotros(request):

	return render(request, 't_nosotros.html')



## es vista se crea la funcion para visualizar un html 
##paso 2° es ir a la urls.py del proyecto "blog"y poner un path('',Home, name='Home') y siempre hay que exportar a la urls.py
