from django.contrib import admin
from .models import Specialty, Specialist, Application
from django.utils.translation import ugettext_lazy as _


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'specialty')

    def specialist(self, obj):
        return '{} {}'.format(obj.name_first, obj.name_last)

    specialist.short_description = _("specialist")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'specialist')
