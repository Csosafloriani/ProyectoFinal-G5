from django import forms
from .models import Noticia
from .models import Denuncia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia']

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['motivo', 'comentario']

