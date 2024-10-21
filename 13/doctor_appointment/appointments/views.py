from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

## serializers
from appointments.serializers import *

## API
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

## REST Authentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

## Override Permission (Custom)
from appointments.permissions import AppointmentsListsPermission, AppointmentsDetailsPermission

# model
from .models import *

class MyTokenAyhtentication(TokenAuthentication):
    keyword = "Bearer"

class DoctorList(APIView):
    authentication_classes = [MyTokenAyhtentication] #เป็นตัวเช็คว่า token ถูกมั๊ย แต่ไม่บังคับ login
    permission_classes = [IsAuthenticated] #บังคับให้ authenticate

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class PatientList(APIView):
    authentication_classes = [MyTokenAyhtentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
class AppointmentList(APIView):
    authentication_classes = [MyTokenAyhtentication]
    permission_classes = [IsAuthenticatedOrReadOnly, AppointmentsListsPermission]

    def get(self, request):
        print("USER:", request.user)
        print("AUTH:", request.auth)
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetail(APIView):
    authentication_classes = [MyTokenAyhtentication]
    permission_classes = [IsAuthenticated, AppointmentsDetailsPermission]
    
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    def put(self, request, pk):
        appointment = Appointment.objects.get(pk=pk)
        self.check_object_permissions(request, appointment)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        appointment = Appointment.objects.get(pk=pk)
        self.check_object_permissions(request, appointment)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
