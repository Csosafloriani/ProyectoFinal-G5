from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields= '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        fields= ('texto', 'usuario')



