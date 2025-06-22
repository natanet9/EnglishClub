from django import forms
from .models import PermisoAusencia

from datetime import date, timedelta


class PermisoAusenciaForm(forms.ModelForm):
    class Meta:
        model = PermisoAusencia
        fields = ['estudiante', 'curso', 'asignatura', 'fecha', 'motivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hoy = date.today()
        un_anio = hoy + timedelta(days=365)

        # Establecer valor inicial y restricciones del input fecha
        self.fields['fecha'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'border rounded px-3 py-2 w-full',
                'min': hoy.isoformat(),
                'max': un_anio.isoformat(),
                'value': hoy.isoformat(),  # valor por defecto visible en el input
            }
        )

        self.fields['motivo'].widget = forms.Textarea(
            attrs={'class': 'border rounded px-3 py-2 w-full', 'rows': 3}
        )