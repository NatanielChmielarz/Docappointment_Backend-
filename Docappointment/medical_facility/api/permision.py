from rest_framework import permissions
from medical_facility.models import MedicalFacility
class MF_AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Sprawdź, czy użytkownik jest zalogowany
        if not request.user.is_authenticated:
            return False

        # Jeśli żądanie jest metodą safe (GET, HEAD, OPTIONS), zezwól na dostęp
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # W przeciwnym razie, sprawdź, czy użytkownik należy do administratorów MedicalFacility
        medical_facility_id = view.kwargs.get('id')
        try:
            medical_facility = MedicalFacility.objects.get(id=medical_facility_id)
        except MedicalFacility.DoesNotExist:
            return False

        # Sprawdź, czy użytkownik należy do administratorów MedicalFacility
        return medical_facility.admins.filter(id=request.user.id).exists()