from django.shortcuts import render, get_object_or_404, redirect
from .models import Asistencia, Inscripcion, Docente
from django.utils.dateparse import parse_date

def listar_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'listar.html', {'asistencias': asistencias})

def registrar_asistencia(request):
    if request.method == 'POST':
        inscripcion_id = request.POST.get('id_inscripcion')
        docente_id = request.POST.get('id_docente')
        fecha = request.POST.get('fecha')
        estado = request.POST.get('estado')

        Asistencia.objects.create(
            id_inscripcion_id=inscripcion_id,
            id_docente_id=docente_id,
            fecha=parse_date(fecha),
            estado=estado
        )
        return redirect('listar_asistencias')

    inscripciones = Inscripcion.objects.all()
    docentes = Docente.objects.all()
    return render(request, 'formulario.html', {
        'inscripciones': inscripciones,
        'docentes': docentes,
        'titulo': 'Registrar Asistencia'
    })

def editar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)

    if request.method == 'POST':
        asistencia.id_inscripcion_id = request.POST.get('id_inscripcion')
        asistencia.id_docente_id = request.POST.get('id_docente')
        asistencia.fecha = parse_date(request.POST.get('fecha'))
        asistencia.estado = request.POST.get('estado')
        asistencia.save()
        return redirect('listar_asistencias')

    inscripciones = Inscripcion.objects.all()
    docentes = Docente.objects.all()
    return render(request, 'formulario.html', {
        'asistencia': asistencia,
        'inscripciones': inscripciones,
        'docentes': docentes,
        'titulo': 'Editar Asistencia'
    })

def eliminar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('listar_asistencias')
    return render(request, 'eliminar_confirmacion.html', {'asistencia': asistencia})
