from django.shortcuts import render, redirect
from .models import Categoria, Noticia, Denuncia
from apps.comentarios.models import Comentario
from apps.usuarios.models import Usuario
from apps.comentarios.forms import ComentarioForm
from .forms import NoticiaForm, DenunciaForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def Listar_Noticias(request):
	contexto = {}

	# Parametros de filtro desde la url
	id_categoria = request.GET.get('id',None)
	fecha = request.GET.get('fecha',None)
	titulo = request.GET.get('titulo',None)

	# Consulta base
	noticias = Noticia.objects.all()

	#aplicar filtro categoria si existe
	if id_categoria:
		noticias = Noticia.objects.filter(categoria_noticia = id_categoria)
	
	
	# Aplicar filtro fecha si existe
	if fecha == 'asc':
		noticias = noticias.order_by('fecha')
	elif fecha == 'desc':
		noticias = noticias.order_by('-fecha')
	
	# Aplicar filtro por tirulo
	if titulo == 'asc':
		noticias = noticias.order_by('titulo')
	elif titulo == 'desc':
		noticias = noticias.order_by('-titulo')

	contexto['noticias'] = noticias

	# Cargar todas las categorías y autores para los campos de selección
	contexto['categorias'] = Categoria.objects.all().order_by('nombre')

	return render(request, 'noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = get_object_or_404(Noticia, pk = pk) #Si la noticia no existe retorna un error
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	#Crear una instancia del formulario de comentarios
	contexto['form'] = ComentarioForm() #se agrega el formulario al contexto

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
#@user_passes_test(lambda u: u.is_staff)
def Eliminar_Noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)

	if request.user == noticia.autor or request.user.is_staff:
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

@login_required
def Denunciar_Noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.noticia = noticia
            denuncia.usuario = request.user
            denuncia.save()
            # Redirigir a la vista de detalles de la noticia o a otro lugar
            return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': pk}))
    else:
        form = DenunciaForm()

    return render(request, 'noticias/denunciar.html', {'form': form, 'noticia': noticia})


#puede borra cualquier usuario la noticia
@login_required
#@user_passes_test(lambda id: id.is_staff)#EL STAFF SOLO PUEDE ELIMINARLA
def Noticia_delete(request, id_noticia):
	noticia= get_object_or_404(Noticia, id=id_noticia)
	if request.method == "POST":  #modifique DELETE POR POST
		noticia.delete() #Noticia o noticia
		return redirect('noticias:listar')
	return render(request, "noticias/noticia_delete.html", {'noticia': noticia})


