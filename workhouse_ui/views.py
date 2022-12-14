from django.shortcuts import render

import requests
import worker_api.models as APIModels
import worker_api.serializers as APISerializers


def registration_page(request):
    return render(request, 'registration.html')


def homepage(request):
    return render(request, 'homepage.html')


def registration(request):
    name = request.GET['name']
    email = request.GET['email']
    password = request.GET['password']
    if request.GET['position'] == 'Manager':
        cat_id = 1
    elif request.GET['position'] == 'Administrator':
        cat_id = 2
    user_info = {
        'name': name,
        'email': email,
        'password': password,
        'cat_id': cat_id
        }
        
    url = 'http://127.0.0.1:8000/api/users/'
    r = requests.post(url, json=user_info)

    return render(request, 'success_page.html')


def log_in_page(request):
    return render(request, 'login.html')


def log_in(request):
    name = request.GET['name']
    password = request.GET['password']

    url = 'http://127.0.0.1:8000/api/users'
    r = requests.get(url)
    users = r.json()['Users']
    for user in users:
        if user['name'] == name and user['password'] == password:
            if user['cat_id'] == 1:
                return render(request, 'administrator_page.html')
    return render(request, 'error.html')
        

def admin_page(request):
    return render(request, 'administrator_page.html')


def get_workers_list(request):
    workers = APIModels.Worker.objects.all()
    return render(request, 'workers.html',context={'Workers': APISerializers.WorkersSerializer(workers, many=True).data})



def create_worker(request):

    new_worker = APIModels.Worker.objects.create(
        name = request.GET['name'],
        work_start_time = request.GET['work_start_time'],
        work_end_time = request.GET['work_end_time']
    )

    return render(request, 'success_page.html')


def get_location_list(request):
    workers = APIModels.Location.objects.all()
    return render(request, 'locations.html',context={'Locations': APISerializers.LocationsSerializer(workers, many=True).data})


def create_location(request):
    new_location = APIModels.Location.objects.create(
        lable = request.GET['lable']
    )
    return render(request, 'success_page.html')

    

def success_page(request):
    return render(request, 'success_page.html')

