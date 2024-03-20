from django.urls import path
from .views import PatientSignupAPIView,PatientProfileView,Disease_history_ListView,Disease_history_CreateView,Disease_historyDeteilsView

urlpatterns = [
    path('register/', PatientSignupAPIView.as_view(), name='patient-register'),
    path('<int:id>', PatientProfileView.as_view(), name='patient-profile'),
    path('<int:id>/Disease_history', Disease_history_ListView.as_view()),
     path('<int:id>/Disease_history-create', Disease_history_CreateView.as_view()),
    path('Disease_history/<int:id>', Disease_historyDeteilsView.as_view())
    # path('/visits
]