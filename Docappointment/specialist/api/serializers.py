
from rest_framework import serializers
from specialist.models import (Specialist,Education,TreatedDisease,
                               Foreign_Languagese,Consultation_Scope,
                               Visit_Type,Reviews)
from django.contrib.auth.hashers import make_password
class Specialist_SignUp_Serializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Specialist
        fields = ['first_name', 'last_name', 'phone_no','main_specialization', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password_mismatch': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        if Specialist.objects.filter(email=validated_data.get("email")).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        password = make_password(validated_data['password'])
        
        return Specialist.objects.create(
            email=validated_data.get("email"),
            password=password,
            main_specialization=validated_data.get("main_specialization"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            phone_no=validated_data.get("phone_no"),
            
        )

        
class Education_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        field='__all__'
        

class Treated_Disease_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TreatedDisease
        fields = '__all__'

class Foreign_Language_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Foreign_Languagese
        fields = '__all__'

class Consultation_Scope_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_Scope
        fields = '__all__'

class Visit_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Visit_Type
        fields = '__all__'


class Reviews_Serializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Reviews
        exclude = ('specialist',)        
        
class Specialist_Serializer(serializers.ModelSerializer):
    specialist_education = Education_Serializer(many=True,read_only=True)
    specialist_treed_disease= Treated_Disease_Serializer(many=True,read_only=True)
    specialist_foreign_languages=Foreign_Language_Serializer(many=True,read_only=True)
    specialist_consultation_scope=Consultation_Scope_Serializer(many=True,read_only=True)
    specialist_visit_type=Visit_Type_Serializer(many=True,read_only=True)
    specialist_reviews=Reviews_Serializer(many=True,read_only=True)
    class Meta:
        model = Specialist
        fields = ["first_name", "last_name", "email","phone_no","photo_no",
                  "specialist_education","specialist_treed_disease",
                  "specialist_foreign_languages","specialist_consultation_scope",
                  "specialist_visit_type","specialist_reviews"]