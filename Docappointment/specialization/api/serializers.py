from rest_framework import serializers
from specialization.models import specialization
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = specialization
        fields= '__all__'