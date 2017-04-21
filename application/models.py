from django.db import models
from .validators import validate_past
from django.utils.translation import ugettext_lazy as _


class Specialty(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("specialty")
        verbose_name_plural = _("specialties")

    def __str__(self):
        return self.name


class Specialist(models.Model):
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('specialty'))
    name_first = models.CharField(max_length=255)
    name_middle = models.CharField(max_length=255, blank=True)
    name_last = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("specialist")
        verbose_name_plural = _("specialists")

    def __str__(self):
        return '{} {}'.format(self.name_first, self.name_last)


class Application(models.Model):
    specialist = models.ForeignKey(Specialist,
                                   on_delete=models.CASCADE,
                                   verbose_name=_('specialist'))
    appointment = models.DateTimeField(validators=[validate_past],
                                       verbose_name=_('appointment time'))
    patient_name_first = models.CharField(max_length=255,
                                          verbose_name=_("patient's first name"))
    patient_name_last = models.CharField(max_length=255,
                                         verbose_name=_("patient's second name"))
    patient_name_middle = models.CharField(max_length=255, blank=True,
                                           verbose_name=_("patient's middle name"))

    class Meta:
        verbose_name = _("application")
        verbose_name_plural = _("applications")
        unique_together = ('appointment', 'specialist')

    def __str__(self):
        return '{:%Y-%m-%d %H:%M}'.format(self.appointment)
