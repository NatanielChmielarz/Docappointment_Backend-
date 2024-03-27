from django.urls import path
from .views import (SpecialistSignupAPIView,Specialist_Profile,Education_CreateView,
                    Education_DetailsView,TreatedDisease_CreateView,TreatedDisease_DetailsView,
                    ForeignLanguage_CreateView,ForeignLaguage_DetailsView,
                    ConsultationScope_CreateView,ConsultationScope_DetailsView,
                    VisitType_CreateView,VisitType_DetailsView,Reviews_ListView,
                    Reviews_CreateView,Reviews_DetailView,Slot_CreateView,Slot_DetailView)
urlpatterns = [
    path('register/',SpecialistSignupAPIView.as_view(),name='register account'),
    path('<int:id>',Specialist_Profile.as_view(), name='specialist_details'),
    path('<int:id>/education-create',Education_CreateView.as_view() ),
    path('education/<int:id>',Education_DetailsView.as_view() ),
    path('<int:id>/TreatedDisease-create',TreatedDisease_CreateView.as_view() ),
    path('TreatedDisease/<int:id>',TreatedDisease_DetailsView.as_view() ),
    path('<int:id>/Foreign_Languagese-create',ForeignLanguage_CreateView.as_view() ),
    path('Foreign_Languagese/<int:id>',ForeignLaguage_DetailsView.as_view() ),
    path('<int:id>/Consultation_Scope-create',ConsultationScope_CreateView.as_view() ),
    path('Consultation_Scope/<int:id>',ConsultationScope_DetailsView.as_view() ),
    path('<int:id>/Visit_Type-create',VisitType_CreateView.as_view() ),
    path('Visit_Type/<int:id>',VisitType_DetailsView.as_view() ),
    path('<int:id>/Reviews',Reviews_ListView.as_view() ),
    path('<int:id>/Reviews-create',Reviews_CreateView.as_view() ),
    path('Reviews/<int:id>', Reviews_DetailView.as_view() ),
    path('<int:id>/Slot-create',Slot_CreateView.as_view() ),
    path('Slot/<int:id>',Slot_DetailView.as_view() ),
    
    
]
