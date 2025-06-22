from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.utils.translation import gettext_lazy as _

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'carnet', 'nombre', 'apellidos', 'rol', 'is_staff', 'is_active')
    list_filter = ('rol', 'is_staff', 'is_active')
    search_fields = ('username', 'nombre', 'apellidos', 'carnet')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información personal'), {'fields': ('carnet', 'nombre', 'apellidos', 'telefono', 'direccion', 'domicilio', 'fecha_nacimiento', 'tutor', 'ocupacion', 'parentesco')}),
        (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Fechas importantes'), {'fields': ('fecha_registro', 'last_login')}),
        (_('Rol'), {'fields': ('rol',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'carnet', 'nombre', 'apellidos', 'password1', 'password2', 'rol', 'is_staff', 'is_active')}
         ),
    )

admin.site.register(Usuario, UsuarioAdmin)
