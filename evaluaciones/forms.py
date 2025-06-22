from django import forms
import random
from .models import EvaluacionDiaria, Nota, TestVak

class EvaluacionDiariaForm(forms.ModelForm):
    class Meta:
        model = EvaluacionDiaria
        fields = ['curso', 'asignatura', 'estudiante', 'is_participate', 'is_tarea', 'is_present']
        labels = {
            'curso': 'Curso Asignado',
            'asignatura': 'Asignatura Evaluada',
            'estudiante': 'Nombre del Estudiante',
            'is_participate': 'Participación',
            'is_tarea': 'Entrega de Tarea',
            'is_present': '¿Asistió?',
        }

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['estudiante', 'asignatura', 'nota_acumulada', 'primer_examen', 'segundo_examen', 'examen_final']
        labels = {
            'estudiante': 'Nombre del Estudiante',
            'asignatura': 'Asignatura',
            'nota_acumulada': 'Nota Acumulada',
            'primer_examen': 'Primer Examen',
            'segundo_examen': 'Segundo Examen',
            'examen_final': 'Examen Final',
        }

class TestVakForm(forms.ModelForm):
    class Meta:
        model = TestVak
        fields = ['visual', 'auditorio', 'lectutura', 'kinestesico', 'estilo_predominante', 'estudiante']
        labels = {
            'visual': 'Porcentaje Visual',
            'auditorio': 'Porcentaje Auditivo',
            'lectutura': 'Porcentaje de Lectura',
            'kinestesico': 'Porcentaje Kinestésico',
            'estilo_predominante': 'Estilo Predominante',
            'estudiante': 'Nombre del Estudiante',
        }

class TestVarkFormE(forms.Form):
   
    PREGUNTAS = [
        {
            'texto': '¿Cómo te gusta aprender algo nuevo?',
            'opciones': [
                ('visual', 'Viendo dibujos o colores.'),
                ('auditivo', 'Escuchando lo que dice la profe.'),
                ('lectura', 'Leyendo con ayuda o solo.'),
                ('kinestesico', 'Haciendo cosas con tus manos.'),
            ]
        },
        {
            'texto': '¿Cómo aprendes a usar un juguete nuevo?',
            'opciones': [
                ('visual', 'Mirando cómo lo hace otro.'),
                ('auditivo', 'Escuchando las instrucciones.'),
                ('lectura', 'Leyendo con ayuda del texto.'),
                ('kinestesico', 'Jugando tú mismo.'),
            ]
        },
        {
            'texto': 'Si haces un dibujo:',
            'opciones': [
                ('visual', 'Te gusta ver muchos colores.'),
                ('auditivo', 'Cantar mientras dibujas.'),
                ('lectura', 'Escribir el nombre del dibujo.'),
                ('kinestesico', 'Usar materiales como goma, pintura o papel.'),
            ]
        },
        {
            'texto': 'Si vas a un lugar nuevo:',
            'opciones': [
                ('visual', 'Ver un mapa o dibujos del sitio.'),
                ('auditivo', 'Escuchar cómo llegar.'),
                ('lectura', 'Leer un letrero.'),
                ('kinestesico', 'Ir caminando tú mismo.'),
            ]
        },
        {
            'texto': '¿Qué prefieres hacer en clase?',
            'opciones': [
                ('visual', 'Ver videos o imágenes.'),
                ('auditivo', 'Escuchar cuentos o canciones.'),
                ('lectura', 'Leer un libro o escribir algo.'),
                ('kinestesico', 'Hacer experimentos o manualidades.'),
            ]
        },
        {
            'texto': 'Si tienes que recordar algo:',
            'opciones': [
                ('visual', 'Dibujas lo que necesitas.'),
                ('auditivo', 'Lo repites en voz alta.'),
                ('lectura', 'Lo escribes en tu cuaderno.'),
                ('kinestesico', 'Lo haces varias veces con tus manos.'),
            ]
        },
        {
            'texto': '¿Qué te gusta más cuando te enseñan inglés?',
            'opciones': [
                ('visual', 'Ver dibujos o colores con las palabras.'),
                ('auditivo', 'Escuchar cómo suenan las palabras.'),
                ('lectura', 'Leer las palabras y copiarlas.'),
                ('kinestesico', 'Jugar usando esas palabras.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando no entiendes algo?',
            'opciones': [
                ('visual', 'Pido que me muestren con dibujos.'),
                ('auditivo', 'Pido que me lo digan otra vez.'),
                ('lectura', 'Leo otra vez o lo escribo.'),
                ('kinestesico', 'Intento hacerlo yo mismo.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta aprender una canción?',
            'opciones': [
                ('visual', 'Viendo el video.'),
                ('auditivo', 'Escuchándola muchas veces.'),
                ('lectura', 'Leyendo la letra.'),
                ('kinestesico', 'Cantándola con gestos y juegos.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando lees un cuento?',
            'opciones': [
                ('visual', 'Miras mucho las imágenes.'),
                ('auditivo', 'Te gusta que alguien te lo lea en voz alta.'),
                ('lectura', 'Te gusta leerlo tú mismo.'),
                ('kinestesico', 'Te gusta actuarlo o jugarlo.'),
            ]
        },
        {
            'texto': '¿Cómo prefieres aprender a sumar?',
            'opciones': [
                ('visual', 'Con dibujos o bloques de colores.'),
                ('auditivo', 'Escuchando a la maestra.'),
                ('lectura', 'Leyendo y haciendo ejercicios.'),
                ('kinestesico', 'Usando fichas o juguetes.'),
            ]
        },
        {
            'texto': '¿Qué prefieres hacer en el recreo?',
            'opciones': [
                ('visual', 'Ver cómo juegan los demás.'),
                ('auditivo', 'Hablar con tus amigos.'),
                ('lectura', 'Leer algo en silencio.'),
                ('kinestesico', 'Correr y jugar mucho.'),
            ]
        },
        {
            'texto': '¿Qué te gusta más de los cuentos?',
            'opciones': [
                ('visual', 'Los dibujos.'),
                ('auditivo', 'Cómo suena la voz del que lo lee.'),
                ('lectura', 'Las palabras que puedes leer.'),
                ('kinestesico', 'Imaginar que eres uno de los personajes.'),
            ]
        },
        {
            'texto': '¿Cómo aprendes mejor una palabra nueva?',
            'opciones': [
                ('visual', 'Viendo un dibujo.'),
                ('auditivo', 'Escuchándola muchas veces.'),
                ('lectura', 'Escribiéndola.'),
                ('kinestesico', 'Usándola en un juego.'),
            ]
        },
        {
            'texto': 'Si tienes que aprender una regla nueva:',
            'opciones': [
                ('visual', 'Quieres verla escrita en la pizarra.'),
                ('auditivo', 'Que la digan varias veces.'),
                ('lectura', 'Leerla tú solo.'),
                ('kinestesico', 'Probarla tú mismo jugando.'),
            ]
        },
        {
            'texto': '¿Qué te gusta más hacer con tus libros?',
            'opciones': [
                ('visual', 'Ver las imágenes.'),
                ('auditivo', 'Leer en voz alta.'),
                ('lectura', 'Leer y escribir con lápiz.'),
                ('kinestesico', 'Hacer cosas con lo que aprendiste.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando te explican un juego?',
            'opciones': [
                ('visual', 'Miras cómo lo juegan.'),
                ('auditivo', 'Escuchas las instrucciones.'),
                ('lectura', 'Lees las reglas.'),
                ('kinestesico', 'Comienzas a jugar para entender.'),
            ]
        },
        {
            'texto': '¿Cómo recuerdas más fácil los colores?',
            'opciones': [
                ('visual', 'Viéndolos en una hoja.'),
                ('auditivo', 'Diciéndolos en voz alta.'),
                ('lectura', 'Leyendo sus nombres.'),
                ('kinestesico', 'Pintando con ellos.'),
            ]
        },
        {
            'texto': '¿Qué te gusta más de los videos?',
            'opciones': [
                ('visual', 'Las imágenes y los colores.'),
                ('auditivo', 'La música o lo que dicen.'),
                ('lectura', 'Leer lo que aparece.'),
                ('kinestesico', 'Imaginarlos y jugarlos después.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta que sea tu cuaderno?',
            'opciones': [
                ('visual', 'Con dibujos y colores.'),
                ('auditivo', 'Con palabras que escuchaste en clase.'),
                ('lectura', 'Con tus propias notas y textos.'),
                ('kinestesico', 'Con recortes o cosas pegadas.'),
            ]
        },
        {
            'texto': 'Cuando haces una manualidad, prefieres:',
            'opciones': [
                ('visual', 'Ver cómo debería quedar.'),
                ('auditivo', 'Que te digan paso a paso.'),
                ('lectura', 'Leer los pasos.'),
                ('kinestesico', 'Hacerlo tú mismo con materiales.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta aprender los números?',
            'opciones': [
                ('visual', 'Viéndolos en una tabla de colores.'),
                ('auditivo', 'Cantándolos.'),
                ('lectura', 'Leyéndolos y escribiéndolos.'),
                ('kinestesico', 'Contando cosas reales.'),
            ]
        },
        {
            'texto': '¿Cómo aprendes los nombres de tus amigos?',
            'opciones': [
                ('visual', 'Viendo sus carteles con dibujos.'),
                ('auditivo', 'Escuchando cuando dicen su nombre.'),
                ('lectura', 'Leyéndolos en su mesa o mochila.'),
                ('kinestesico', 'Jugando con ellos.'),
            ]
        },
        {
            'texto': '¿Qué te gusta más de las clases?',
            'opciones': [
                ('visual', 'Las láminas y colores.'),
                ('auditivo', 'Las canciones o historias.'),
                ('lectura', 'Leer en voz baja.'),
                ('kinestesico', 'Participar en actividades.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando aprendes algo nuevo?',
            'opciones': [
                ('visual', 'Lo dibujas.'),
                ('auditivo', 'Lo dices en voz alta.'),
                ('lectura', 'Lo escribes en tu cuaderno.'),
                ('kinestesico', 'Lo juegas o haces una actividad.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta aprender los días de la semana?',
            'opciones': [
                ('visual', 'Viéndolos en un cartel con colores.'),
                ('auditivo', 'Escuchando una canción.'),
                ('lectura', 'Leyéndolos en un cuaderno.'),
                ('kinestesico', 'Jugando con tarjetas.'),
            ]
        },
        {
            'texto': '¿Qué te ayuda más a entender un cuento nuevo?',
            'opciones': [
                ('visual', 'Ver los dibujos del cuento.'),
                ('auditivo', 'Escuchar cómo lo lee alguien.'),
                ('lectura', 'Leerlo tú mismo.'),
                ('kinestesico', 'Actuarlo con tus amigos.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando estás aburrido?',
            'opciones': [
                ('visual', 'Miras libros con imágenes.'),
                ('auditivo', 'Cantas o hablas con alguien.'),
                ('lectura', 'Escribes o dibujas algo.'),
                ('kinestesico', 'Juegas con tus juguetes.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta aprender los colores en inglés?',
            'opciones': [
                ('visual', 'Viendo tarjetas de colores.'),
                ('auditivo', 'Escuchando canciones de colores.'),
                ('lectura', 'Leyendo los nombres de colores.'),
                ('kinestesico', 'Coloreando cosas.'),
            ]
        },
        {
            'texto': '¿Qué actividad disfrutas más en el aula?',
            'opciones': [
                ('visual', 'Ver láminas en la pizarra.'),
                ('auditivo', 'Escuchar cuentos.'),
                ('lectura', 'Escribir o leer.'),
                ('kinestesico', 'Hacer juegos o trabajos en grupo.'),
            ]
        },
        {
            'texto': '¿Cómo te preparas para un show escolar?',
            'opciones': [
                ('visual', 'Miras cómo lo hacen otros niños.'),
                ('auditivo', 'Escuchas bien lo que dice la profe.'),
                ('lectura', 'Lees tus líneas o letras.'),
                ('kinestesico', 'Practicas moviéndote o actuando.'),
            ]
        },
        {
            'texto': '¿Qué te ayuda a recordar una historia?',
            'opciones': [
                ('visual', 'Ver dibujos de los personajes.'),
                ('auditivo', 'Escuchar la historia otra vez.'),
                ('lectura', 'Leerla muchas veces.'),
                ('kinestesico', 'Jugar a que eres un personaje.'),
            ]
        },
        {
            'texto': '¿Cómo prefieres aprender el abecedario?',
            'opciones': [
                ('visual', 'Viendo letras grandes con dibujos.'),
                ('auditivo', 'Escuchando una canción del ABC.'),
                ('lectura', 'Leyendo y escribiendo las letras.'),
                ('kinestesico', 'Formando letras con plastilina.'),
            ]
        },
        {
            'texto': '¿Cómo entiendes mejor una nueva palabra?',
            'opciones': [
                ('visual', 'Viendo un dibujo de la palabra.'),
                ('auditivo', 'Escuchando su pronunciación.'),
                ('lectura', 'Leyéndola en una frase.'),
                ('kinestesico', 'Usándola en un juego o actividad.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando tienes una tarea?',
            'opciones': [
                ('visual', 'Dibujas algo sobre el tema.'),
                ('auditivo', 'Pides que te expliquen en voz alta.'),
                ('lectura', 'Lees lo que dice la consigna.'),
                ('kinestesico', 'Haces una maqueta o trabajo manual.'),
            ]
        },
        {
            'texto': '¿Cómo prefieres aprender formas (círculo, cuadrado...)?',
            'opciones': [
                ('visual', 'Viéndolas dibujadas.'),
                ('auditivo', 'Diciéndolas en voz alta.'),
                ('lectura', 'Leyendo su nombre.'),
                ('kinestesico', 'Cortándolas o armándolas.'),
            ]
        },
        {
            'texto': 'Si vas al zoológico, ¿qué te gusta más?',
            'opciones': [
                ('visual', 'Ver a los animales.'),
                ('auditivo', 'Escuchar lo que cuentan sobre ellos.'),
                ('lectura', 'Leer los carteles de información.'),
                ('kinestesico', 'Darles comida o imitarlos.'),
            ]
        },
        {
            'texto': '¿Cómo aprendes mejor una poesía?',
            'opciones': [
                ('visual', 'Viendo los gestos o dibujos.'),
                ('auditivo', 'Escuchando su ritmo y rima.'),
                ('lectura', 'Leyéndola muchas veces.'),
                ('kinestesico', 'Actuándola o diciendo con mímica.'),
            ]
        },
        {
            'texto': '¿Cómo prefieres decorar tu carpeta?',
            'opciones': [
                ('visual', 'Pegando dibujos o colores.'),
                ('auditivo', 'Escribiendo lo que dice la profe.'),
                ('lectura', 'Escribiendo tu nombre y clase.'),
                ('kinestesico', 'Poniendo stickers o cosas que hiciste.'),
            ]
        },
        {
            'texto': '¿Qué parte del cuaderno usas más?',
            'opciones': [
                ('visual', 'Donde están las imágenes.'),
                ('auditivo', 'Donde anotas lo que escuchas.'),
                ('lectura', 'Donde escribes cuentos o textos.'),
                ('kinestesico', 'Donde haces dibujos o pegas cosas.'),
            ]
        },
        {
            'texto': 'Si vas a hacer una exposición en clase:',
            'opciones': [
                ('visual', 'Dibujas algo para mostrar.'),
                ('auditivo', 'Ensayas lo que vas a decir.'),
                ('lectura', 'Escribes todo en tu hoja.'),
                ('kinestesico', 'Haces un cartel o una maqueta.'),
            ]
        },
        {
            'texto': '¿Qué te gusta más en la televisión?',
            'opciones': [
                ('visual', 'Ver los colores y personajes.'),
                ('auditivo', 'Escuchar canciones o voces divertidas.'),
                ('lectura', 'Leer subtítulos o nombres.'),
                ('kinestesico', 'Imitar lo que hacen.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta aprender a cuidar el medio ambiente?',
            'opciones': [
                ('visual', 'Viendo imágenes de la naturaleza.'),
                ('auditivo', 'Escuchando historias sobre animales.'),
                ('lectura', 'Leyendo cuentos ecológicos.'),
                ('kinestesico', 'Plantando o reciclando.'),
            ]
        },
        {
            'texto': '¿Qué actividad te gusta más en inglés?',
            'opciones': [
                ('visual', 'Ver dibujos y repetir las palabras.'),
                ('auditivo', 'Escuchar una historia en inglés.'),
                ('lectura', 'Leer una pequeña frase.'),
                ('kinestesico', 'Hacer un juego o actividad.'),
            ]
        },
        {
            'texto': '¿Cómo recuerdas mejor los nombres de animales?',
            'opciones': [
                ('visual', 'Viendo sus fotos.'),
                ('auditivo', 'Escuchando cómo se llaman.'),
                ('lectura', 'Leyendo sus nombres.'),
                ('kinestesico', 'Jugando a imitarlos.'),
            ]
        },
        {
            'texto': 'Si haces un dibujo libre:',
            'opciones': [
                ('visual', 'Te gusta usar muchos colores.'),
                ('auditivo', 'Cantar mientras dibujas.'),
                ('lectura', 'Escribir tu nombre o título.'),
                ('kinestesico', 'Usar materiales nuevos.'),
            ]
        },
        {
            'texto': '¿Qué haces cuando te enseñan una nueva palabra en inglés?',
            'opciones': [
                ('visual', 'Miras una tarjeta con dibujos.'),
                ('auditivo', 'Repites la palabra en voz alta.'),
                ('lectura', 'La escribes en tu hoja.'),
                ('kinestesico', 'La usas jugando o actuando.'),
            ]
        },
        {
            'texto': '¿Qué prefieres en un libro?',
            'opciones': [
                ('visual', 'Las imágenes.'),
                ('auditivo', 'Escuchar el cuento.'),
                ('lectura', 'Leer con ayuda.'),
                ('kinestesico', 'Tocar, mover o actuar lo que pasa.'),
            ]
        },
        {
            'texto': '¿Cómo te gusta repasar para una prueba?',
            'opciones': [
                ('visual', 'Usando dibujos o colores.'),
                ('auditivo', 'Diciendo las cosas en voz alta.'),
                ('lectura', 'Releyendo y subrayando.'),
                ('kinestesico', 'Haciendo juegos o actividades.'),
            ]
        },
        {
            'texto': '¿Qué te hace sentir más feliz al aprender?',
            'opciones': [
                ('visual', 'Ver cosas bonitas y coloridas.'),
                ('auditivo', 'Escuchar cosas divertidas.'),
                ('lectura', 'Leer cosas interesantes.'),
                ('kinestesico', 'Hacer cosas con las manos.'),
            ]
        },
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        selected_questions = random.sample(self.PREGUNTAS, 16)
  
        for i, pregunta in enumerate(selected_questions, 1):
            self.fields[f'pregunta_{i}'] = forms.ChoiceField(
                label=pregunta['texto'],
                choices=[(op[0], op[1]) for op in pregunta['opciones']],
                widget=forms.RadioSelect,
                required=True
            )