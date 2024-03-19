from django.db import models
from user_app.models import User
from specialization.models import specialization
# class MedicalFacilityAdmin(User):
#     class Meta:
#         proxy = True
        
        
# class MedicalFacility(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     website = models.URLField(blank=True, null=True)
#     specialties = models.ManyToManyField(specialization, related_name='medical_facilities')
#     specialists = models.ManyToManyField(specialist, related_name='specialist_facilities')
#     def __str__(self):
#         return self.name