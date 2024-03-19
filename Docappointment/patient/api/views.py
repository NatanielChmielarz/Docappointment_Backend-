from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView,Response,status
from rest_framework.views import Response
from rest_framework.views import status
from .serializers import PatientSerializer
from rest_framework import generics
from patient.models import Patient
from .serializers import PatientSerializer
class PatientSignupAPIView(APIView):
    permission_classes = []

    def post(self, request):
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        
        if password == confirm_password:
            serializer = PatientSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
            response_status = status.HTTP_201_CREATED
        else:
            data = ''
            raise ValidationError({'password_mismatch': 'Password fields did not match.'})
        
        return Response(data, status=response_status)
    
class PatientProfileView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field='id'
    permission_classes=[]
    