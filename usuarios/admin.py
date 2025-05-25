from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('carnet', 'nombre', 'apellidos', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'rol')
    fieldsets = (
        (None, {'fields': ('carnet', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellidos', 'direccion', 'telefono', 'fecha_nacimiento', 'hijo', 'domicilio', 'rol', 'ocupacion', 'parentesco')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('carnet', 'nombre', 'apellidos', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('carnet', 'nombre', 'apellidos')
    ordering = ('carnet',)
