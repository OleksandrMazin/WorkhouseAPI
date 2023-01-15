from rest_framework import serializers
from worker_api import models
import datetime


class WorkersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Worker
        fields = "__all__"

class WorksSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Work
        fields = "__all__"

class LocationsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = models.Location
        fields = "__all__"

class AppointmentsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        all_appointments = models.Appointment.objects.all()
        for appointment in all_appointments:
            if data['worker'] == appointment.worker:
                if data['date'] == appointment.date:
                    #TODO add whole time check
                    if data['time'] == appointment.time or data['time'] == datetime.datetime.now():
                        raise serializers.ValidationError({'time': 'this time is reserved'})
        return data
                

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Appointment
        fields = "__all__"

class ScheduleSerializer(serializers.Serializer):
    client_name = serializers.CharField(max_length=100)
    client_phone = serializers.CharField(max_length=13)
    record_date = serializers.DateField()
    record_time = serializers.TimeField()
    location = serializers.CharField(max_length=255)
    worker = serializers.CharField(max_length=255)
    type_of_work = serializers.CharField(max_length=30)
