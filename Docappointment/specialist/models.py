from datetime import timezone
from django.db import models
from django.forms import ValidationError
from user_app.models import User
from patient.models import Patient
from specialization.models import specialization
from django.core.validators import  MinValueValidator,MaxValueValidator
from medical_facility.models import MedicalFacility
# Create your models here.
class Specialist(User):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_no = models.CharField(max_length =9)
    main_specialization = models.ForeignKey(specialization,on_delete=models.CASCADE,related_name='specialist_specializations')
    about_me = models.TextField(blank=True)
    photo_no = models.CharField(max_length =100,blank=True)
    avg_rating = models.FloatField(default=0,blank=True)
    number_rating = models.IntegerField(default=0,blank=True)
    def __str__(self):
        return self.first_name +' ' + self.last_name
#wyksztalcenie
class Education(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_education")
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
#leczone choroby
class TreatedDisease(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_treed_disease")
    disease_name = models.CharField(max_length=100)
# jezyki obce
class Foreign_Languagese(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_foreign_languages")
    language_name = models.CharField(max_length=100)
#zakres porad
class Consultation_Scope(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_consultation_scope")
    scope_name = models.CharField(max_length=100)
# rodzaje wizyt
class Visit_Type(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_visit_type")
    visit_type_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self):
        return self.visit_type_name
# opinie    
class Reviews(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_reviews")
    review_user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class SpecialistSlots(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name="specialist_slot")
    visit_type = models.ForeignKey(Visit_Type,on_delete=models.CASCADE, related_name="slot_visit_type")
    address = models.ForeignKey(MedicalFacility, on_delete=models.CASCADE, related_name="medical_facility_address")
    date_time = models.DateTimeField()
    duration_minutes = models.IntegerField(validators=[MinValueValidator(1)])
    active = models.BooleanField(blank=True, default=True)
    def __str__(self):
        return f"{self.specialist.first_name} {self.specialist.last_name} - {self.visit_type.name} - {self.date_time}"

    def clean(self):
        if self.address not in self.specialist.medical_facilities.all():
            raise ValidationError("Adress must be in specialist.medical_facilities")
        if self.date_time <= timezone.now():
            raise ValidationError("the date must be greater than the current time ")
        if self.specialist not in self.visit_type.specialist.all():
            raise ValidationError("Specialist doesn't offer this visit type")
