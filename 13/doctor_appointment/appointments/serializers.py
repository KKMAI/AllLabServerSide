from rest_framework import serializers
from .models import *
from datetime import date, datetime

# one
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "phone_number",
            "email"
        ]

# one
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "phone_number",
            "email",
            "address"
        ]

## many
class AppointmentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance) #ได้เป็น json แล้ว จริง ตอน create, update ไม่ได้มีผลอะไร มันแค่มาดึงตอนสุดท้ายไปแสดงผลเฉยๆ

        representation['doctor'] = DoctorSerializer(instance.doctor).data #มันไปดึง object มาแสดง
        representation['patient'] = PatientSerializer(instance.patient).data #มันไปดึง object มาแสดง
        # ตรงกับชื่อ field ใน Appointment

        return representation
    
    class Meta:
        model = Appointment
        fields = ["id", "doctor", "patient", "date", "at_time", "details", "created_by"] #มัน overide ModelSerializer ก็ใช้ได้ "doctor", "patient"

    def validate(self, data):
        datetime_combine = datetime.combine(data['date'], data['at_time'])
        if datetime_combine < datetime.now():
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        return data
    

