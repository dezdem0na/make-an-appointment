import factory
from . import models
from django.utils import timezone
from faker import Factory
fake = Factory.create()


class SpecialtyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Specialty

    name = factory.Faker('job')


class SpecialistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Specialist

    specialty = factory.SubFactory(SpecialtyFactory)
    name_first = factory.Faker('first_name')
    name_last = factory.Faker('last_name')
    name_middle = factory.Faker('first_name')


class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Application

    specialist = factory.SubFactory(SpecialistFactory)
    appointment = fake.date_time_this_year(before_now=False, after_now=True,
                                           tzinfo=timezone.get_current_timezone())

    patient_name_first = factory.Faker('first_name')
    patient_name_last = factory.Faker('last_name')
    patient_name_middle = factory.Faker('first_name')
