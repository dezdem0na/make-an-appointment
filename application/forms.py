from django import forms
from application.models import Application, Specialist
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'appointment': forms.DateTimeInput(
                attrs={'class': 'datetimepicker',
                       'autocomplete': 'off',
                       'value': (timezone.localtime(timezone.now()).replace(hour=9, minute=0))
                                .strftime('%Y-%m-%d %H:%M')}
            )
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': _("Sorry, this time slot is not available."),
            }
        }


class SpecialistForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SpecialistForm, self).__init__(*args, **kwargs)
        self.fields['specialty'].required = False

    class Meta:
        model = Specialist
        fields = ["specialty", ]

