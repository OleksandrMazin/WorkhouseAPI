from django.contrib import admin
from django.urls import path, include

import worker_api.views as WorkerAPI
from user_api.views import UserAPI
from workhouse_ui import views as UIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserAPI)
router.register(r'workers', WorkerAPI.WorkersAPIView)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', UIView.homepage),
    
    path('homepage/', UIView.homepage, name='homepage'),
    path('registration/', UIView.registration_page, name='registration'),
    path('register/', UIView.registration, name='register'),
    path('login_page/', UIView.log_in_page, name='login_page'),
    path('login/', UIView.log_in, name='login'),
    path('administrator_page/', UIView.admin_page, name='admin_page'),
    path('create_worker/', UIView.create_worker, name='create_worker'),
    path('workers/', UIView.get_workers_list, name='get_workers'),
    path('locations/', UIView.get_location_list, name='locations'),
    path('create_location/', UIView.create_location, name='create_location'),
    path('schedule/', UIView.get_schedule, name='schedule'),
    path('create_appointment/', UIView.create_appointment, name='create_appointment'),
    
    path('success/', UIView.success_page, name='success'),

    path('api/', include(router.urls)),
    path('api/works/', WorkerAPI.WorksAPIView.as_view()),
    path('api/locations/', WorkerAPI.LocationAPIView.as_view()),
    path('api/appointments/', WorkerAPI.AppointmentsAPIView.as_view()),
    path('api/schedule/', WorkerAPI.ScheduleAPIView.as_view()),
]
