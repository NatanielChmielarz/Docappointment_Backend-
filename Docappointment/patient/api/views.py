from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView,Response,status
from rest_framework.views import Response
from rest_framework.views import status
from .serializers import PatientSerializer
from rest_framework import generics
from patient.models import Patient,Disease_history
from .serializers import PatientSerializer,Disease_history_Serializer
from .permision import PatientUserOrReadOnly
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
    permission_classes=[PatientUserOrReadOnly]
    
class Disease_history_ListView(generics.ListAPIView):
    serializer_class = Disease_history_Serializer
    permission_classes = [PatientUserOrReadOnly]
    def get_queryset(self):
        id = self.kwargs['id']
        return Disease_history.objects.filter(Patient=id)
      
class Disease_history_CreateView(generics.CreateAPIView):
    serializer_class = Disease_history_Serializer
    permission_classes = [PatientUserOrReadOnly]
    def get_queryset(self):
        return Disease_history.objects.all()
    def perform_create(self, serializer):
        id = self.kwargs['id']
        patient= Patient.objects.get(id=id)
       
        serializer.save(Patient=patient)
class Disease_historyDeteilsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disease_history.objects.all()
    serializer_class = Disease_history_Serializer
    lookup_field='id'
    permission_classes = [PatientUserOrReadOnly]    