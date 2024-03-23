from django.urls import path
from .views import (CreateMedicalFacility,AddSpecialistToMedicalFacility,AddAdminToMedicalFacility,MedicalFacilityDetail)
urlpatterns = [
    path("CreateMedicalFacility/",CreateMedicalFacility.as_view()),
    path("<int:id>/Add-Admin",AddAdminToMedicalFacility.as_view()),
    path("<int:id>",MedicalFacilityDetail.as_view()),
    path("<int:id>/Add-Specialist/<int:specialist_id>",AddSpecialistToMedicalFacility.as_view()),
]
