from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Comentario
from .forms import ComentarioForm
from apps.noticias.models import Noticia

@login_required
def agregar_comentario(request, noticia_id, comentario_id=None):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    parent_comentario = None

    if comentario_id: # si se está respondiendo a un comentario
        parent_comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.noticia = noticia
            comentario.parent = parent_comentario # si es una respuesta asignar el comentario padre
        
            comentario.save()
        return redirect('noticias:detalle', pk=noticia_id)
    
    else:
        form = ComentarioForm()
    
    return render(request, 'comentarios/agregar_comentario.html', {'form': form, 'noticia':noticia, 'parent_comentario': parent_comentario})

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    #Solo el autor o el admin pueden eliminar el comentario

    if request.user == comentario.usuario or request.user.is_superuser or request.user.is_staff:
        comentario.delete()
    
    return redirect('noticias:detalle', pk=comentario.noticia.id)
