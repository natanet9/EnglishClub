from django.shortcuts import render
from evaluaciones.models import TestVak, EvaluacionDiaria
from cursos.models import Curso
from usuarios.models import Usuario
from collections import Counter
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import io

def vista_reportes(request):
    varks = TestVak.objects.all()
    evaluaciones = EvaluacionDiaria.objects.all()
    cursos = Curso.objects.all()
    usuarios = Usuario.objects.all()

    # Filtros
    usuario_id = request.GET.get('usuario')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Filtrar VARK y Evaluaciones por usuario
    if usuario_id:
        varks = varks.filter(estudiante__id=usuario_id)
        evaluaciones = evaluaciones.filter(estudiante__id=usuario_id)

    # Filtrar Evaluaciones por fecha
    if fecha_inicio:
        evaluaciones = evaluaciones.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        evaluaciones = evaluaciones.filter(fecha__lte=fecha_fin)

    # Conteo de resultados VARK
    tipos_vark = ["Visual", "Auditivo", "Kinestésico", "Lectura/Escritura"]
    conteo_vark = [varks.filter(estilo_predominante=tipo).count() for tipo in tipos_vark]

    contexto = {
        'varks': varks,
        'evaluaciones': evaluaciones,
        'cursos': cursos,
        'usuarios': usuarios,
        'tipos_vark': tipos_vark,
        'conteo_vark': conteo_vark,
    }
    return render(request, 'reporteria/vista_reportes.html', contexto)

# Exportar a Excel con filtros aplicados
def exportar_excel(request):
    varks = TestVak.objects.select_related('estudiante')

    usuario_id = request.GET.get('usuario')
    if usuario_id:
        varks = varks.filter(estudiante__id=usuario_id)

    data = varks.values('estudiante__username', 'estilo_predominante')
    df = pd.DataFrame(data)

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=reportes_vark.xlsx'
    df.to_excel(response, index=False)
    return response

# Exportar a PDF con filtros aplicados
def exportar_pdf(request):
    varks = TestVak.objects.all()

    usuario_id = request.GET.get('usuario')
    if usuario_id:
        varks = varks.filter(estudiante__id=usuario_id)

    buffer = io.BytesIO()
    fig, ax = plt.subplots()

    conteo = Counter(varks.values_list('estilo_predominante', flat=True))
    ax.bar(conteo.keys(), conteo.values(), color=['#7e57c2', '#42a5f5', '#66bb6a', '#ffa726'])
    plt.title("Resultados VARK")
    plt.xlabel("Estilo de Aprendizaje")
    plt.ylabel("Cantidad de estudiantes")

    fig.tight_layout()
    fig.savefig(buffer, format='pdf')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
