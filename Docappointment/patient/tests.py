import unittest
from django.urls import reverse
from django.test import Client, RequestFactory
from user_app.models import User
from patient.models import Patient
from specialist.models import SpecialistSlots
from .models import VisitReservation
from .api.views import VisitReservationDetailsView

class TestPatientModel(unittest.TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(email='test32@o2.pl', password='testpassword',first_name="name",last_name="last_name",phone_no="441334113")
    def test_create_patient(self):
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(self.patient.email, 'test32@o2.pl')
    def test_update_patient(self):
        self.patient.first_name = "Test_johny"
        self.patient.save()
        self.assertEqual(self.patient.first_name, "Test_johny")
    def test_delete_patient(self):
        self.patient.delete()
        self.assertEqual(Patient.objects.count(), 0)
