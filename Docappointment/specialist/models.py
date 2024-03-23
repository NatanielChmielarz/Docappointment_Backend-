from django.db import models
from user_app.models import User
from patient.models import Patient
from specialization.models import specialization
from django.core.validators import  MinValueValidator,MaxValueValidator
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
# opinie    
class Reviews(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,related_name="specialist_reviews")
    review_user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
