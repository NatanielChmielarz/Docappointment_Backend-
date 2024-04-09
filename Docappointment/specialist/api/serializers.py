
import datetime
from rest_framework import serializers
from specialist.models import (Specialist,Education,TreatedDisease,
                               Foreign_Languagese,Consultation_Scope,
                               Visit_Type,Reviews,SpecialistSlots)
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
        exclude=('specialist',)
        

class Treated_Disease_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TreatedDisease
        exclude=('specialist',)

class Foreign_Language_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Foreign_Languagese
        exclude=('specialist',)

class Consultation_Scope_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_Scope
        exclude=('specialist',)

class Visit_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Visit_Type
        exclude=('specialist',)


class Reviews_Serializer(serializers.ModelSerializer):
    review_user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Reviews
        exclude = ('specialist',)        
class SlotDisplaySerializer(serializers.ModelSerializer):
    specialist = serializers.StringRelatedField(read_only=True)
    visit_type = serializers.StringRelatedField()
    address = serializers.StringRelatedField()
    
    class Meta:
        model = SpecialistSlots 
        fields='__all__'
        
    
 

class SlotCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistSlots 
        exclude = ('specialist',)     
        
class Specialist_Serializer(serializers.ModelSerializer):
    specialist_education = Education_Serializer(many=True,read_only=True)
    specialist_treed_disease= Treated_Disease_Serializer(many=True,read_only=True)
    specialist_foreign_languages=Foreign_Language_Serializer(many=True,read_only=True)
    specialist_consultation_scope=Consultation_Scope_Serializer(many=True,read_only=True)
    specialist_visit_type=Visit_Type_Serializer(many=True,read_only=True)
    specialist_reviews=Reviews_Serializer(many=True,read_only=True)
    specialist_slot = SlotDisplaySerializer(many=True,read_only=True)
    main_specialization= serializers.StringRelatedField(read_only=True)
    specialist_facilities = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Specialist
        fields = ["first_name", "last_name", "email","phone_no",
                  "specialist_education","specialist_treed_disease",
                  "specialist_foreign_languages","specialist_consultation_scope",
                  "specialist_visit_type",'main_specialization',"specialist_reviews",'avg_rating','number_rating','specialist_slot','specialist_facilities']
    def get_active_slots(self, instance):
        return instance.specialist_slot.filter(active=True, date_time__gt=datetime.datetime.now())
  
    def to_representation(self, instance):
        
        representation = super().to_representation(instance)
        representation['specialist_slot'] = SlotDisplaySerializer(
            self.get_active_slots(instance), many=True).data
        return representation