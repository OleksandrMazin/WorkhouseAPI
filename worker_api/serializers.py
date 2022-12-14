from rest_framework import serializers


class WorkersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    work_start_time = serializers.TimeField()
    work_end_time = serializers.TimeField()

class WorksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 30)
    duration = serializers.TimeField()

class LocationsSerializer(serializers.Serializer):
    lable = serializers.CharField(max_length=255)

class AppointmentsSerializer(serializers.Serializer):
    client_name = serializers.CharField(max_length=100)
    client_phone = serializers.CharField(max_length=13)
    worker_id = serializers.IntegerField()
    location_id = serializers.IntegerField()
    work_id = serializers.IntegerField()
    date = serializers.DateField()
    time = serializers.TimeField()

class ScheduleSerializer(serializers.Serializer):
    client_name = serializers.CharField(max_length=100)
    client_phone = serializers.CharField(max_length=13)
    record_date = serializers.DateField()
    record_time = serializers.TimeField()
    location = serializers.CharField(max_length=255)
    worker = serializers.CharField(max_length=255)
    type_of_work = serializers.CharField(max_length=30)
