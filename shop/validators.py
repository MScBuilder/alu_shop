from email import message
from unicodedata import category
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class MaxWidthValidator(BaseValidator):
    def __init__(self, limit_value, message=None, cat=None):
        self.limit_value = limit_value
        if cat:
            self.cat = cat
        if message:
            self.message = message

    message = _("Ensure this value is less than or equal to %(limit_value)s.")
    code = "max_value"

    def compare(self, a, b ):
        return a > b