from django.db import models

class Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()

class Tarea(models.Model):
    '''
    modelo que representa la tarea de un proyecto
    '''

    PRIORIDAD_CHOICES =[
        ('BAJA','Baja'),
        ('MEDIA','Media'),
        ('ALTA','Alta'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE','Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
    ]

    Proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='tareas'
    )

    titulo = models.CharField(max_length=50)
    prioridad = models.CharField(
        max_length=5,
        choices=PRIORIDAD_CHOICES,
        default='MEDIA',
    )
    estado = models.CharField(
        max_length=11,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
    )