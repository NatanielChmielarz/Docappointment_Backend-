
from rest_framework import generics
from specialization.models import specialization
from specialization.api.serializers import SpecializationSerializer
class SpecializationView(generics.ListCreateAPIView):
    queryset = specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = []
class SpecializationDetailsView(generics.RetrieveUpdateAPIView):
    queryset = specialization.objects.all()
    serializer_class = SpecializationSerializer
    lookup_field = 'id'
    permission_classes = []