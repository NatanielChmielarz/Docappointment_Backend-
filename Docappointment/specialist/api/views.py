from django.shortcuts import render
from rest_framework.views import APIView,Response,status
from rest_framework.views import Response
from rest_framework.views import status
from .serializers import (Specialist_SignUp_Serializer,Specialist_Serializer,Education_Serializer,Treated_Disease_Serializer,
                          Foreign_Language_Serializer,Consultation_Scope_Serializer,
                          Visit_Type_Serializer,Reviews_Serializer)
from rest_framework import generics
from specialist.models import (Specialist,Education,TreatedDisease,
                               Foreign_Languagese,Consultation_Scope,
                               Visit_Type,Reviews)
from django.forms import ValidationError
from .permision import SpecialistOrReadOnly
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