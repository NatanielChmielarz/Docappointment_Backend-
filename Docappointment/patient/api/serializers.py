from rest_framework import serializers
from patient.models import Patient,Disease_history
from django.contrib.auth.hashers import make_password
class PatientSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password_mismatch': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        if Patient.objects.filter(email=validated_data.get("email")).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        password = make_password(validated_data['password'])
        return Patient.objects.create(
            
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            phone_no=validated_data.get("phone_no"),
            email=validated_data.get("email"),
            password=password
        )
class Disease_history_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Disease_history
        fields= '__all__'