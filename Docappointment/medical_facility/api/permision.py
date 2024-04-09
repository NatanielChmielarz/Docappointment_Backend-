from rest_framework import permissions
from medical_facility.models import MedicalFacility
class MF_AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

  
        medical_facility_id = view.kwargs.get('id')
        try:
            medical_facility = MedicalFacility.objects.get(id=medical_facility_id)
        except MedicalFacility.DoesNotExist:
            return False

       
        return medical_facility.admins.filter(id=request.user.id).exists()