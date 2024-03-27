from django.shortcuts import render
from rest_framework.views import APIView,Response,status
from rest_framework.views import Response
from rest_framework.views import status
from .serializers import (Specialist_SignUp_Serializer,Specialist_Serializer,Education_Serializer,Treated_Disease_Serializer,
                          Foreign_Language_Serializer,Consultation_Scope_Serializer,
                          Visit_Type_Serializer,Reviews_Serializer,SlotCreateUpdateSerializer)
from rest_framework import generics
from specialist.models import (Specialist,Education,TreatedDisease,
                               Foreign_Languagese,Consultation_Scope,
                               Visit_Type,Reviews,SpecialistSlots)
from django.forms import ValidationError
from .permision import SpecialistOrReadOnly,ReviewUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from patient.models import Patient
# Create your views here.
class SpecialistSignupAPIView(APIView):
    permission_classes = []

    def post(self, request):
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        
        if password == confirm_password:
            serializer = Specialist_SignUp_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
            response_status = status.HTTP_201_CREATED
        else:
            data = ''
            raise ValidationError({'password_mismatch': 'Password fields did not match.'})
        
        return Response(data, status=response_status)
    
class Specialist_Profile(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Specialist.objects.all()
    serializer_class = Specialist_Serializer
    lookup_field='id'
    permission_classes = [SpecialistOrReadOnly]
    
    
class Education_CreateView(generics.CreateAPIView):
    serializer_class = Education_Serializer
    permission_classes = [SpecialistOrReadOnly]
    def get_queryset(self):
        return Education.objects.all()
    def perform_create(self, serializer):
        id = self.kwargs['id']
        specialist= Specialist.objects.get(id=id)
       
        serializer.save(specialist=specialist)
    
class Education_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = Education_Serializer
    lookup_field='id'
    permission_classes = [SpecialistOrReadOnly]

class TreatedDisease_CreateView(generics.CreateAPIView):
    queryset = TreatedDisease.objects.all()
    schema = Treated_Disease_Serializer
    permission_classes = [SpecialistOrReadOnly]
    def perform_create(self, serializer):
        id = self.kwargs['id']
        specialist= Specialist.objects.get(id=id)
       
        serializer.save(specialist=specialist)
    
class TreatedDisease_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreatedDisease.objects.all()
    serializer_class = Treated_Disease_Serializer
    lookup_field='id'
    permission_classes = [SpecialistOrReadOnly]
    
class ForeignLanguage_CreateView(generics.CreateAPIView):
    queryset = Foreign_Languagese.objects.all()
    serializer_class = Foreign_Language_Serializer
    permission_classes = [SpecialistOrReadOnly]
    def perform_create(self, serializer):
        id = self.kwargs['id']
        specialist= Specialist.objects.get(id=id)
       
        serializer.save(specialist=specialist)
    
class ForeignLaguage_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Foreign_Languagese.objects.all()
    serializer_class = Foreign_Language_Serializer
    lookup_field='id'
    permission_classes = [SpecialistOrReadOnly]
    
class ConsultationScope_CreateView(generics.CreateAPIView):
    queryset = Consultation_Scope.objects.all()
    serializer_class = Consultation_Scope_Serializer
    permission_classes = [SpecialistOrReadOnly]
    def perform_create(self, serializer):
        id = self.kwargs['id']
        specialist= Specialist.objects.get(id=id)
       
        serializer.save(specialist=specialist)
    
class ConsultationScope_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation_Scope.objects.all()
    serializer_class = Consultation_Scope_Serializer
    lookup_field='id'
    permission_classes = [SpecialistOrReadOnly]
    
class VisitType_CreateView(generics.CreateAPIView):
    queryset = Visit_Type.objects.all()
    serializer_class = Visit_Type_Serializer
    permission_classes = [SpecialistOrReadOnly]
    def perform_create(self, serializer):
        id = self.kwargs['id']
        specialist= Specialist.objects.get(id=id)
       
        serializer.save(specialist=specialist)
class VisitType_DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit_Type.objects.all()
    serializer_class = Visit_Type_Serializer
    lookup_field='id'
    permission_classes = [SpecialistOrReadOnly]
    

class Reviews_ListView(generics.ListAPIView):
    serializer_class = Reviews_Serializer  
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        id = self.kwargs['id']
        return Reviews.objects.filter(specialist=id)    
    
class Reviews_CreateView(generics.CreateAPIView):
    serializer_class = Reviews_Serializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Reviews.objects.all()
    def perform_create(self, serializer):
        id = self.kwargs['id']
        Specialist_= Specialist.objects.get(id=id)
        review_user = Patient.objects.get(id=self.request.user.id)
        review_queryset = Reviews.objects.filter(specialist=Specialist_,review_user=review_user) 
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this Specialist_")
        if Specialist_.number_rating == 0:
            Specialist_.avg_rating = serializer.validated_data['rating']
        else:
            Specialist_.avg_rating = (Specialist_.avg_rating*Specialist_.number_rating + serializer.validated_data['rating'])/2
        
        Specialist_.number_rating = Specialist_.number_rating + 1
        Specialist_.save()
        serializer.save(specialist=Specialist_,review_user=review_user)
class Reviews_DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = Reviews_Serializer  
    lookup_field='id'
    permission_classes = [ReviewUserOrReadOnly]
    
class Slot_CreateView(generics.CreateAPIView):
    
     serializer_class = SlotCreateUpdateSerializer
     def perform_create(self, serializer):
        id = self.kwargs['id']
        Specialist_= Specialist.objects.get(id=id)
        serializer.save(specialist=Specialist_)
class Slot_DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpecialistSlots.objects.all()
    serializer_class =SlotCreateUpdateSerializer 
    lookup_field='id'
    permision_classes = [SpecialistOrReadOnly]
   