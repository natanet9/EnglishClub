from django import forms
from .models import PermisoAusencia

from datetime import date, timedelta


from django import forms
from datetime import date, timedelta
from .models import PermisoAusencia

class PermisoAusenciaForm(forms.ModelForm):
    class Meta:
        model = PermisoAusencia
        fields = ['estudiante', 'curso', 'asignatura', 'fecha', 'motivo']
        widgets = {
            'motivo': forms.Textarea(attrs={'class': 'border rounded px-3 py-2 w-full', 'rows': 3}),
        }
        labels = {
            'motivo': 'Motivo de la ausencia',
            'fecha': 'Fecha de la ausencia',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Estudiante deshabilitado
        if user:
            self.fields['estudiante'].initial = user
            self.fields['estudiante'].disabled = True
            self.fields['estudiante'].widget.attrs['class'] = 'border rounded px-3 py-2 w-full bg-gray-100 cursor-not-allowed'

        # Rango dinámico para el input tipo date
        hoy = date.today()
        max_fecha = hoy + timedelta(days=14)
        self.fields['fecha'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'border rounded px-3 py-2 w-full',
                'min': hoy.strftime('%Y-%m-%d'),
                'max': max_fecha.strftime('%Y-%m-%d'),
            }
        )

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        hoy = date.today()
        max_fecha = hoy + timedelta(days=30)

        if not (hoy <= fecha <= max_fecha):
            raise forms.ValidationError("La fecha debe estar dentro de los próximos 30 días.")
        return fecha

