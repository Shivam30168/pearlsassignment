# models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    max_patients = models.IntegerField()
    available_days = models.JSONField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_day = models.DateField()

    def __str__(self):
        return f"{self.doctor.name}'s appointment on {self.appointment_day}"
