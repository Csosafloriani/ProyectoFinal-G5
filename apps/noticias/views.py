
#from django.shortcuts import get_object_or_404

#from django. http import HttpResponse
#from django. template import loader 


from django.shortcuts import render, redirect
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria, Comentario

from .forms import NoticiaForm

from django.urls import reverse_lazy

@login_required
def Listar_Noticias(request):
	contexto = {}

	id_categoria = request.GET.get('id',None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticia = id_categoria)
	else:
		n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS

	contexto['noticias'] = n

	cat = Categoria.objects.all().order_by('nombre')
	contexto['categorias'] = cat

	return render(request, 'noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(id=1)#RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE '''

"""def noticia (request):
	noticias_list=Noticia.object.all()
	template=loader.get_template ("listar.html")
	context={"noticias_list":noticias_list}
	return HttpResponse (template.render (context, request))"""


@login_required 
def agregar_noticia(request):
	if request.method=='POST':
		form=NoticiaForm(request.POST)
		if form.is_valid():
			noticia= form.save(commit=False)
			noticia.autor=request.usuario
			noticia.save()
			return redirect ('noticias')
		else:
			form=NoticiaForm()
	return render(request, 'noticias/agregar_noticia.html',
		{'noticia':noticia})
		

@login_required 
def editar_noticia(request, pk):
	noticia=Noticia.objects.get(pk=pk)
	if request.method=='POST':
		form=NoticiaForm(request.POST, instance=noticia)
		if form.is_valid():
			form.save()
			return redirect ('noticias')
		else:
			form=NoticiaForm(instance=noticia)
	return render(request, 'noticias/editar_noticia.html',
		{'noticia':noticia})

@login_required 
def eliminar_noticia(request, pk):
	noticia=Noticia.objects.get(pk=pk)
	if request.method=='POST':
		noticia.delete()
		return redirect('noticias')
	return render(request, 'noticias/eliminar_noticia.html',
			{'noticia':noticia})
    


def get_succes_url(self):
	return reverse_lazy("noticias:Listar_Noticias")


