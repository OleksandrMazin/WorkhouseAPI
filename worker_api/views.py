from django.db import connection
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import worker_api.serializers as Serial

from .models import Appointment, Location, Work, Worker


class WorkersAPIView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = Serial.WorkersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WorksAPIView(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = Serial.WorksSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class LocationAPIView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = Serial.LocationsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class AppointmentsAPIView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = Serial.AppointmentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ScheduleAPIView(generics.ListAPIView):
    serializer_class = Serial.ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

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