from django.db import models
from user_app.models import User
from specialization.models import specialization
# from specialist.models import Specialist
class MedicalFacilityAdmin(User):
    class Meta:
        proxy = True
        
        
class MedicalFacility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default="Poland")
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    specialties = models.ManyToManyField(specialization, related_name='medical_facilities',blank=True)
    specialists = models.ManyToManyField('specialist.Specialist', related_name='specialist_facilities',blank=True)
    admins = models.ManyToManyField(MedicalFacilityAdmin, related_name='medicalFacilityAdmin')
    def __str__(self):
        return self.name + ' ' + self.city + ' ' + self.address