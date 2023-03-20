from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db import models

class MinimumLengthValidator:
    def __init__(self, min_length=0):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(_("This password must at contain as least %(min_length)d characters."), code='password_too_short', params={'min_length': self.min_length},)

    def get_help_text(self):
        return _("Your password must contain at least %(min_length)d characters." % {'min_length': self.min_length})

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(_('%(value)s is not an even number'), params={'value': value})
