from django.test import TestCase
from django.urls import reverse_lazy

from application.forms import ApplicationForm
from application.models import Application
from application import factories
import factory
from faker import Factory
from django.utils import timezone
fake = Factory.create()


class FormTest(TestCase):
    def setUp(self):
        self.specialist = factories.SpecialistFactory()
        self.application = factories.ApplicationFactory()

    def test_valid_form(self):
        supplier = Application()
        supplier_form = ApplicationForm({
            'specialist': self.specialist.pk,
            'appointment': fake.date_time_this_year(before_now=False, after_now=True,
                                                    tzinfo=timezone.get_current_timezone()),
            'patient_name_first': factory.Faker('first_name'),
            'patient_name_last': factory.Faker('last_name'),
        },
            instance=supplier)
        self.assertTrue(supplier_form.is_valid())

    def test_invalid_blank_form(self):
        data = {}
        supplier = Application()
        supplier_form = ApplicationForm(data, instance=supplier)
        self.assertFalse(supplier_form.is_valid())

    def test_invalid_date_form(self):
        supplier = Application()
        supplier_form = ApplicationForm({
            'specialist': self.specialist.pk,
            'appointment': fake.date_time_this_year(before_now=True, after_now=False,
                                                    tzinfo=timezone.get_current_timezone()),
            'patient_name_first': factory.Faker('first_name'),
            'patient_name_last': factory.Faker('last_name'),
        },
            instance=supplier)
        self.assertFalse(supplier_form.is_valid())

