
from rest_framework import permissions

class PatientUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
class PatientVisitOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
       
        return obj.Patient.id == request.user.id or obj.reservation_info.specialist.id==request.user.id
    

            