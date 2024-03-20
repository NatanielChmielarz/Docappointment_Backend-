from django.urls import path
from .views import (SpecialistSignupAPIView,Specialist_Profile)
urlpatterns = [
    path('register/',SpecialistSignupAPIView.as_view(),name='register account'),
    path('<int:id>',Specialist_Profile.as_view(), name='account')
   
    #path('<int:id>/education-create', name=')
    #path('education/<int:id>', name=')
    #path('<int:id>/TreatedDisease-create', name=')
    #path('TreatedDisease/<int:id>', name=')
    #path('<int:id>/Foreign_Languagese-create', name=')
    #path('Foreign_Languagese/<int:id>', name=')
    #path('<int:id>/Consultation_Scope-create', name=')
    #path('Consultation_Scope/<int:id>', name=')
    #path('<int:id>/Visit_Type-create', name=')
    #path('Visit_Type/<int:id>', name=')
    #path('<int:id>/Reviews-create', name=')
    #path('Reviews/<int:id>', name=')
    
    
]
