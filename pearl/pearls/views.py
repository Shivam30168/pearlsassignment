# views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class BookAppointment(generics.CreateAPIView):
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        doctor_id = request.data.get('doctor')
        appointment_day = request.data.get('appointment_day')
        
        doctor = Doctor.objects.get(pk=doctor_id)
        
        if appointment_day not in doctor.available_days:
            return Response({'message': 'Doctor is not available on this day'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Appointment.objects.filter(doctor=doctor, appointment_day=appointment_day).count() >= doctor.max_patients:
            return Response({'message': 'Doctor has reached the maximum number of patients for this day'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
