from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


def validate_past(value):

    if value < timezone.now():
        raise ValidationError(
            _('Sorry, this time slot is not available.'),
        )
