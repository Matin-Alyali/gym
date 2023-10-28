from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import UserRegistration
# Create your views here.

class UserRegisterView(APIView):
    
    def post(self, request, *args, **kwargs):
        ser_data = UserRegistration(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                username= ser_data.validated_data['username'],
                email= ser_data.validated_data['email'],
                password = ser_data.validated_data['password'],
            )
            return Response('success',status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)