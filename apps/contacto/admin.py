from django.contrib import admin
from .models import Contacto

# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    list_display=('id','nombre_apellido', 'email', 'aunto', 'fecha',)
    search_fields=['id','nombre_apellido', 'email', 'asunto', 'fecha',]# busca por todo


admin.site.register(Contacto, ContactoAdmin)
