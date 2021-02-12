from django.db import models

# Create your models here.
class Patient(models.Model):
    pass

class Doctor(models.Model):
    Patients = [Patient() for i in range(100)]