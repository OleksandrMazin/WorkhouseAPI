from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

import worker_api.views as WorkerAPI
from workhouse_ui import views as UIView

router = routers.DefaultRouter()
router.register(r'workers', WorkerAPI.WorkersAPIView)
router.register(r'works', WorkerAPI.WorksAPIView)
router.register(r'locations', WorkerAPI.LocationAPIView)
router.register(r'appointments', WorkerAPI.AppointmentsAPIView)


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

    path('api/', include(router.urls), name='api'),
    path('api/schedule/', WorkerAPI.ScheduleAPIView.as_view()),
    path('api/auth/', include('rest_framework.urls')),
]
