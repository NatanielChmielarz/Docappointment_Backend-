from django.db import models
from user_app.models import User
# Create your models here.

class Patient(User):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length =9)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Disease_history(models.Model):
    diseanse = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="Patient_diseanse_history")
    def __str__(self):
        return self.diseanse
    
class VisitReservation(models.Model):
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="patient_visit_reservation")
    reservation_info = models.ForeignKey('specialist.SpecialistSlots', on_delete=models.CASCADE,related_name="ReservationInfo") 
    