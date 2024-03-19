from django.urls import path
from .views import PatientSignupAPIView,PatientProfileView

urlpatterns = [
    path('register/', PatientSignupAPIView.as_view(), name='patient-register'),
    path('<int:id>', PatientProfileView.as_view(), name='patient-profile'),
    # path('<int:id>/Disease_history', Disease_historyListView.as_view(), name
    # path('<int:id>/Disease_history/<int:id>', Disease_historyDeteilsView.as_view(), name
    # path('/visits
]