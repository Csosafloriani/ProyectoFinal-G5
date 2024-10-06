from django import forms 
from .models import Noticia # Personaje es el modelo extraido de models

class NoticiaForm(forms.ModelForm):
	class Meta:
		model=Noticia
		fields= '__all__'
