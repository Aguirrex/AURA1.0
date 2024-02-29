from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import *
import datetime

# Create your views here.

@login_required
def salas(request):
    
    
    salas = Sala.objects.all()
    equipos = Equipo.objects.all()
    horas = [datetime.time(6,0),datetime.time(6,30),datetime.time(7,0),datetime.time(7,30),datetime.time(8,0),datetime.time(8,30),datetime.time(9,0),datetime.time(9,30),datetime.time(10,0),datetime.time(10,30),datetime.time(11,0),datetime.time(11,30),datetime.time(12,0),datetime.time(12,30),datetime.time(13,0),datetime.time(13,30),datetime.time(14,0),datetime.time(14,30),datetime.time(15,0),datetime.time(15,30),datetime.time(16,0),datetime.time(16,30),datetime.time(17,0),datetime.time(17,30),datetime.time(18,0),datetime.time(18,30),datetime.time(19,0),datetime.time(19,30),datetime.time(20,0),datetime.time(20,30),datetime.time(21,0),datetime.time(21,30),datetime.time(22,0)]

    if 'sala_id' in request.GET:
        sala_id = request.GET['sala_id']
        sala = Sala.objects.get(id=sala_id)
        equipos = equipos.filter(sala_id=sala)

        #reservas has a foreign key to equipo and equipo has a foreign key to sala
        reservas = ReservaEstudiantes.objects.all().filter(equipo_id__sala_id=sala_id)

        data_table = []

        for i in range(0, len(horas)):
            data_row = []
            data_row.append(horas[i])
            for j in range(0, len(equipos)):
                try:
                    reserva = reservas.filter(equipo_id=equipos[j],hora_reserva=horas[i])
                except:
                    reserva = None

                if reserva:
                    data = (reserva[0].id,Estudiante.objects.all().filter(id = reserva[0].estudiante_id).first().cc )
                    data_row.append(data)
                else:
                    data_row.append(("",""))
            data_table.append(data_row)


        context = {'salas':salas, 'equipos':equipos, 'sala':sala, 'data_table':data_table}
    else:
        context = {'salas':salas , 'equipos':None , 'data_table' : None}

    if 'reserva_id' in request.GET:
        reserva_id = request.GET['reserva_id']
        reserva = ReservaEstudiantes.objects.get(id=reserva_id)

        nombre_info = Estudiante.objects.get(id=reserva.estudiante_id).nombre
        codigo_info = Estudiante.objects.get(id=reserva.estudiante_id).cc
        dependencia_info = Estudiante.objects.get(id=reserva.estudiante_id).dependencia
        equipo_info = Equipo.objects.get(id=reserva.equipo_id)
        hora_info = reserva.hora_reserva


        context = {'salas':salas, 'equipos':equipos, 'sala':sala, 'data_table':data_table, 'nombre_info':nombre_info, 'codigo_info':codigo_info, 'dependencia_info':dependencia_info, 'equipo_info':equipo_info, 'hora_info':hora_info}

   
    return render(request,'Aura/salas.html',context)

def get_information(request):
    codigo = request.GET['codigo']
    try:
        estudiante = Estudiante.objects.get(cc=codigo)
        reserva = ReservaEstudiantes.objects.get(estudiante_id=estudiante)
        context = {'estudiante':estudiante, 'reserva':reserva}
        return JsonResponse(context)
    except:
        return JsonResponse({'error':'No se encontro el estudiante'})

@login_required
def cubiculos(request):
    context = {}
    return render(request,'Aura/cubiculos.html')
