from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required, user_passes_test


from .models import Noticia, Categoria
from apps.comentarios.models import Comentario

from .forms import NoticiaForm
from django.urls import reverse_lazy


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

	n = get_object_or_404(Noticia, pk = pk) #Si la noticia no existe retorna un error
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK

	if not com or not noti: #verificamos que existan todos los datos
		return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))
	
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK

	Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

#Crear noticias
@login_required
def Crear_Noticia(request):
		if request.method == "POST":
			form = NoticiaForm(request.POST, request.FILES)
			if form.is_valid():
				noticia = form.save(commit=False)
				noticia.autor = request.user #asigna el autor
				noticia.save()
				return redirect(reverse_lazy( 'noticias:listar'))
		else:
			form = NoticiaForm()
		
		return render(request, 'noticias/crear.html', {'form':form})

@login_required
def Editar_Noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)

	if request.user != noticia.autor and not request.user.is_staff: #para que solo el autor o el admin puedan editar
		return redirect('noticias:detalle', pk=pk)
	
	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES, instance=noticia)
		if form.is_valid():
			form.save()
			return redirect('noticias:detalle', pk=noticia.pk)
	else:
		form =NoticiaForm(instance=noticia)
	
	return render(request, 'noticias/editar.html', {'form': form, 'noticia': noticia})

@login_required
@user_passes_test(lambda u: u.is_staff)
def Eliminar_Noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	noticia.delete()
	return redirect('noticias:listar')

#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''