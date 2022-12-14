from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# class UsersAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UsersAPIView(generics.ListAPIView):

    def get(self, request):
        lst = User.objects.all().values()
        return Response({'Users': list(lst)})
        
#TODO name/email check
    def post(self, request):
        register = User.objects.create(
            name = request.data['name'],
            email = request.data['email'],
            password = request.data['password'],
            cat_id = request.data['cat_id']
        )

        return Response({'post': model_to_dict(register)})