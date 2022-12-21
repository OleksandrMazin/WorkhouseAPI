from rest_framework import serializers
from worker_api import models


class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = "__all__"

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Work
        fields = "__all__"

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = "__all__"

class AppointmentsSerializer(serializers.ModelSerializer):
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
