from django.contrib import admin
from .models import Worker, Work, Location, Appointment

admin.site.register(Worker)
admin.site.register(Work)
admin.site.register(Location)
admin.site.register(Appointment)