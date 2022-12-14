from django.contrib import admin
from django.urls import path

import worker_api.views as WorkerAPI
from user_api.views import UsersAPIView
from workhouse_ui import views as UIView

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
    
    path('success/', UIView.success_page, name='success'),

    path('api/users/', UsersAPIView.as_view()),
    path('api/workers/', WorkerAPI.WorkersAPIView.as_view()),
    path('api/works/', WorkerAPI.WorksAPIView.as_view()),
    path('api/locations/', WorkerAPI.LocationAPIView.as_view()),
    path('api/appointments/', WorkerAPI.AppointmentsAPIView.as_view()),
    path('api/schedule/', WorkerAPI.ScheduleAPIView.as_view()),
]
