from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria, Comentario

from django.urls import reverse_lazy

from .forms import NoticiaForm



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

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
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
CLASE.objects.all() ---> SELECT * FROM CLASE

'''


@login_required
def Noticia_form(request):
	context= { 'form': NoticiaForm() }
	if request.method == "POST":
		form=NoticiaForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			context["mensaje"]= "se guardo el form"
			return redirect("noticias:cargar_noticia") # noticias= la url que se define en la urls.py de la apps
	else: 
		context["mensaje"]= "CARGAR"
		#context['form']= form
		
	return render(request,"noticias/carga_noticia.html", context ) # y crear un html en template de la apps de noticia
#editar

@login_required
def Noticia_editar(request, id_noticia):
	noticia = get_object_or_404(Noticia, id=id_noticia)
	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES, instance=noticia)
		if form.is_valid():
			form.save()
			return redirect('noticias:detalle', id_noticia )
	else:
		form =NoticiaForm(instance=noticia)
	return render(request, 'noticias/editar_noticia.html', {'form': form, 'noticia': noticia})

#puede borra cualquier usuario la noticia
@login_required
#@user_passes_test(lambda id: id.is_staff)#EL STAFF SOLO PUEDE ELIMINARLA
def Noticia_delete(request, id_noticia):
	noticia= get_object_or_404(Noticia, id=id_noticia)
	if request.method == "POST":  #modifique DELETE POR POST
		noticia.delete() #Noticia o noticia
		return redirect('noticias:listar')
	return render(request, "noticias/noticia_delete.html", {'noticia': noticia})


