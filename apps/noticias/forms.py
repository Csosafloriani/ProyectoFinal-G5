from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo','categoria_noticia', 'cuerpo', 'imagen']

