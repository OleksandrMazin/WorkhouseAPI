from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db import connection
import datetime

from .models import Worker, Work, Location, Appointment
import worker_api.serializers as Serial



class WorkersAPIView(generics.ListAPIView):
    def get(self, request):
        workers = Worker.objects.all()
        return Response({'Workers': Serial.WorkersSerializer(workers, many=True).data})

    def post(self, request):

        serializer = Serial.WorkersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_worker = Worker.objects.create(
            name = request.data['name'],
            work_start_time = request.data['work_start_time'],
            work_end_time = request.data['work_end_time']
        )

        return Response({'post': Serial.WorkersSerializer(new_worker).data})


class WorksAPIView(generics.ListAPIView):
    def get(self, request):
        works = Work.objects.all()
        return Response({'Works': Serial.WorksSerializer(works, many=True).data})

    def post(self, request):

        serializer = Serial.WorksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_work = Work.objects.create(
            title = request.data['title'],
            duration = request.data['duration']
        )

        return Response({'post': Serial.WorksSerializer(new_work).data})


class LocationAPIView(generics.ListAPIView):
    def get(self, request):
        locations = Location.objects.all()
        return Response({'Locations': Serial.LocationsSerializer(locations, many=True).data})

    def post(self, request):
    
        serializer = Serial.LocationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_work = Location.objects.create(
            lable = request.data['lable'],
        )

        return Response({'post': Serial.LocationsSerializer(new_work).data})


class AppointmentsAPIView(generics.ListAPIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        return Response({'Appointments': Serial.AppointmentsSerializer(appointments, many=True).data})

    def post(self, request):

        serializer = Serial.AppointmentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_appointment = Appointment.objects.create(
            client_name = request.data['client_name'],
            client_phone = request.data['client_phone'],
            worker_id = request.data['worker_id'],
            location_id = request.data['location_id'],
            work_id = request.data['work_id'],
            date = request.data['date'],
            time = request.data['time']

        )

        return Response({'post': Serial.AppointmentsSerializer(new_appointment).data})
        

class ScheduleAPIView(generics.ListAPIView):
    
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