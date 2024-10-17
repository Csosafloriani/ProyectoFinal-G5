from django.contrib import admin

from django.contrib import admin
from .models import Contacto

# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    list_display=('id','nombre_apellido', 'email', 'aunto', 'fecha',)


admin.site.register(Contacto)
