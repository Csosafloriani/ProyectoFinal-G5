from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
admin.site.register(Usuario, UserAdmin)
from .models import Usuario #hice from

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['id', 'last_login', 'username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
    search_fields=['id', 'first_name', 'last_name', 'username', 'email', 'is_staff']




