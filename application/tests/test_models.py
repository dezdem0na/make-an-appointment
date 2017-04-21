from django.test import TestCase
from application import models
from application import factories


class ModelTest(TestCase):
    def setUp(self):
        self.specialty = factories.SpecialtyFactory()
        self.specialist = factories.SpecialistFactory()
        self.application = factories.ApplicationFactory()

    def test_specialty_creation(self):
        self.assertTrue(isinstance(self.specialty, models.Specialty))

    def test_specialist_creation(self):
        self.assertTrue(isinstance(self.specialist, models.Specialist))

    def test_application_creation(self):
        self.assertTrue(isinstance(self.application, models.Application))
