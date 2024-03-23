
from rest_framework import serializers
from medical_facility.models import MedicalFacility,MedicalFacilityAdmin
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from specialist.api.views import Specialist_Profile
class Medical_Facility_Serializer(serializers.ModelSerializer):
    specialties = serializers.StringRelatedField(many=True, read_only=True)
    specialists = serializers.SerializerMethodField()

    class Meta:
        model = MedicalFacility
        fields = ["name", "address", "city", "phone_number", "email", "specialties", "specialists"]

    def get_specialists(self, obj):
        specialists = obj.specialists.all()
        request = self.context.get('request')
        specialist_dict = {}
        if request is not None:
            for specialist in specialists:
                if specialist.main_specialization:
                    specialization_name = str(specialist.main_specialization)
                    specialist_url = request.build_absolute_uri(f'/account/Specialist/{specialist.id}')
                    specialist_dict.setdefault(specialization_name, []).append((specialist.__str__(), specialist_url))
        return specialist_dict
class MedicalFacilityAdminSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_style':'password'},write_only=True)
    class Meta:
        model= MedicalFacilityAdmin
        fields=('email','password','confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self,validated_data):
        if MedicalFacilityAdmin.objects.filter(email=self.validated_data.get("email")).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        if validate_password(validated_data['password']) == None:
               password = make_password(validated_data['password'])
               account = MedicalFacilityAdmin.objects.create(email=validated_data.get("email"),password=password)
        return account
   