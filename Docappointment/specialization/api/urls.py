from django.urls import path
from specialization.api.views import SpecializationView,SpecializationDetailsView
urlpatterns = [
    path('',SpecializationView.as_view() ),
    path('<int:id>',SpecializationDetailsView.as_view() )
]
