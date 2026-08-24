from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from .models import Proyecto, Tarea


def home(request):
    return render(request, 'home.html')

def mostrar_proyectos(request):
    proyectos =  Proyecto.objects.all()

    nombre_proyectos = list()

    for p in proyectos:
        nombre_proyectos.append(p.nombre)

    return HttpResponse(nombre_proyectos)

def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})


def nuevos_registros(request):
    proyectos = [
        Proyecto(nombre='Aplicacion de bancaria', descripcion='Aplicacion web para gestionar cuentas bancarias', duracion=1000),
        Proyecto(nombre='Aplicacion de mensajeria', descripcion='Aplicacion para enviar mensajes de textos', duracion=100),
        Proyecto(nombre='Tienda virtual', descripcion='Aplicacion web para comprar y vender productos en linea', duracion=700),
    ]

    for p in proyectos:
        p.save()
    
    return HttpResponse('Registros guardados.')

def ver_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

def nuevo_proyecto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')

        if nombre and descripcion and duracion:
            proyecto = Proyecto(
                nombre=nombre,
                descripcion=descripcion,
                duracion=duracion
            )
            proyecto.save()

            return redirect('proyectos')

    return render(request, 'nuevo-proyecto.html')

def eliminar_proyecto(request, id):
    proyecto=Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyectos')

def editar_proyecto(request, id):
    proyecto= Proyecto.objects.get(id=id)

    if request.method =="POST":
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        duracion=request.POST.get('duracion')

        if nombre and descripcion and duracion:
            proyecto.nombre = nombre
            proyecto.descripcion = descripcion
            proyecto.duracion = int(duracion)
            proyecto.save()

            return redirect('ver_proyecto', id=proyecto.id)

    return render(request, 'editar-proyecto.html', {'proyecto':proyecto})

def crear_tarea(request, proyecto_id):
    proyecto = get_list_or_404(Proyecto, id=proyecto_id)

    if request.method =="POST":
        pass

    datos= {
        'proyecto': proyecto,
        'prioridad_choices': Tarea.PRIORIDAD_CHOICES,
        'estado_choices': Tarea.ESTADO_CHOICES
    }

    return render(request, 'crear-tarea.html', datos)