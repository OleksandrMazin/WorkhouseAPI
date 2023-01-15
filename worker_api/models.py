from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    name = models.CharField(max_length=255, unique=True)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Work(models.Model):
    title = models.CharField(max_length=50, unique=True)
    duration = models.TimeField()
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Location(models.Model):
    lable = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.lable


class Appointment(models.Model):
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=13)
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT)
    location = models.ForeignKey('Location', on_delete=models.PROTECT)
    work = models.ForeignKey('Work', on_delete=models.PROTECT)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name + ' ' + str(self.work) + ' ' + str(self.date) + ' ' + str(self.time )

