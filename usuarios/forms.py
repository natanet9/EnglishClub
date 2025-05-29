from django import forms
from .models import Usuario

class EstudianteTecnicoForm(forms.ModelForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    direccion = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = Usuario
        exclude = ['hijo', 'parentesco', 'is_staff', 'is_active', 'fecha_registro','rol']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class EstudianteRegularForm(forms.ModelForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    direccion = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = Usuario
        exclude = ['hijo', 'parentesco', 'ocupacion', 'is_staff', 'is_active', 'fecha_registro','rol']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class TutorForm(forms.ModelForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    direccion = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = Usuario
        exclude = ['parentesco', 'is_staff', 'is_active', 'fecha_registro', 'rol']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class AdministrativoForm(forms.ModelForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    direccion = forms.EmailField(label="Correo electrónico")
    rol = forms.ChoiceField(
        label="Rol",
        choices=[
            ('docente', 'Docente'),
            ('directivo', 'Directivo'),
            ('secretaria', 'Secretaria'),
        ]
    )

    class Meta:
        model = Usuario
        exclude = ['hijo', 'parentesco', 'is_staff', 'is_active', 'fecha_registro']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }