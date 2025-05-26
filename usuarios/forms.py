from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'carnet',
            'nombre',
            'apellidos',
            'direccion',
            'telefono',
            'fecha_nacimiento',
            'hijo',
            'domicilio',
            'rol',
            'ocupacion',
            'parentesco',
            'is_active',
            'is_staff'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'username': 'Nombre de usuario',
            'carnet': 'Carnet de identidad',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'hijo': 'Información de hijos',
            'domicilio': 'Domicilio',
            'rol': 'Rol',
            'ocupacion': 'Ocupación',
            'parentesco': 'Parentesco',
            'is_active': '¿Está activo?',
            'is_staff': '¿Es miembro del staff?',
        }