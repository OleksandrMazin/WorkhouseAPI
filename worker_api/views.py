from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.db import connection
import datetime

from .models import Worker, Work, Location, Appointment
import worker_api.serializers as Serial



class WorkersAPIView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = Serial.WorkersSerializer


class WorksAPIView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = Serial.WorksSerializer


class LocationAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = Serial.LocationsSerializer


class AppointmentsAPIView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = Serial.AppointmentsSerializer
        

class ScheduleAPIView(generics.ListAPIView):
    serializer_class = Serial.ScheduleSerializer
    
    all_data = {'Schedule': []}
    with connection.cursor() as cursor:
        cursor.execute("""SELECT client_name, client_phone, date, time, worker_api_location.lable,
                            worker_api_worker.name, worker_api_work.title
                            FROM worker_api_appointment JOIN worker_api_location 
                            ON location_id=worker_api_location.id
                            JOIN worker_api_worker ON worker_id=worker_api_worker.id
                            JOIN worker_api_work ON work_id=worker_api_work.id""")
        row = cursor.fetchall()
        
    for elem in row:
        record = {
            'client_name': elem[0],
            'client_phone': elem[1],
            'record_date': elem[2].strftime('%d/%m/%Y'),
            'record_time': elem[3].strftime('%H:%M'),
            'location': elem[4],
            'worker': elem[5],
            'type_of_work': elem[6]
        }

        all_data['Schedule'].append(record)

    def get(self, request):
        return Response({'Schedule': Serial.ScheduleSerializer(self.all_data['Schedule'], many=True).data})

    def get_shedule(self):
        return self.all_data