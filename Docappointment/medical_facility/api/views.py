from rest_framework import generics
from .permision import MF_AdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from medical_facility.models import MedicalFacility
from medical_facility.models import MedicalFacility,MedicalFacilityAdmin
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from specialist.models import Specialist
from .serializers import MedicalFacilityAdminSerializer,Medical_Facility_Serializer
class CreateMedicalFacility(generics.CreateAPIView):
    queryset = MedicalFacility.objects.all()
    permission_classes = []

    def create(self, request, *args, **kwargs):
        admin_email = request.data.get('admin_email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        name = request.data.get('name')
        address = request.data.get('address')
        city = request.data.get('city')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')

        if not all([admin_email, password, confirm_password, name, address, city, phone_number, email]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        if MedicalFacilityAdmin.objects.filter(email=admin_email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        password_hash = make_password(password)
        admin = MedicalFacilityAdmin.objects.create(email=admin_email, password=password_hash)

        
        medical_facility = MedicalFacility.objects.create(
            name=name,
            address=address,
            city=city,
            phone_number=phone_number,
            email=email
        )
        medical_facility.admins.add(admin)

        return Response({'success': 'Medical facility created successfully'}, status=status.HTTP_201_CREATED)
    
class AddSpecialistToMedicalFacility(generics.UpdateAPIView):
    queryset = MedicalFacility.objects.all()
    permission_classes=[MF_AdminOrReadOnly]
    def update(self, request, *args, **kwargs):
        
        medical_facility_id = kwargs.get('id')
        specialist_id = kwargs.get('specialist_id')

        try:
            medical_facility = MedicalFacility.objects.get(id=medical_facility_id)
            specialist = Specialist.objects.get(id=specialist_id)
        except MedicalFacility.DoesNotExist:
            return Response({'error': 'Medical facility does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Specialist.DoesNotExist:
            return Response({'error': 'Specialist does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if medical_facility.specialists.filter(id=specialist_id).exists():
            return Response({'error': 'Specialist already exists in the medical facility'}, status=status.HTTP_400_BAD_REQUEST)
    
        medical_facility.specialists.add(specialist)
        main_specialization = specialist.main_specialization

        if main_specialization and main_specialization not in medical_facility.specialties.all():
            print(main_specialization)
            medical_facility.specialties.add(main_specialization)
        return Response({'success': f'Specialist added to medical facility {medical_facility_id} successfully'},
                        status=status.HTTP_200_OK)

class AddAdminToMedicalFacility(generics.CreateAPIView):
    queryset = MedicalFacilityAdmin.objects.all()
    permission_classes = [MF_AdminOrReadOnly]
    serializer_class = MedicalFacilityAdminSerializer

    def create(self, request, *args, **kwargs):
        medical_facility_id = kwargs.get('id')

        try:
            medical_facility = MedicalFacility.objects.get(id=medical_facility_id)
        except MedicalFacility.DoesNotExist:
            return Response({'error': 'Medical facility does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        admin = serializer.save()

        medical_facility.admins.add(admin)

        return Response({'success': 'New admin was added to Medical Facility'}, status=status.HTTP_200_OK)
class MedicalFacilityDetail(generics.RetrieveAPIView):
    queryset = MedicalFacility.objects.all()
    serializer_class = Medical_Facility_Serializer
    lookup_field = 'id'
    permission_classes = []
          
        
