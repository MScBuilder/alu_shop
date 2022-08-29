from django import forms
from django.forms import ModelForm
from . import models

#creating Construction form
class ConstructionForm(forms.ModelForm):
    class Meta:
        model = models.Construction
        fields = ('category', 'reference_name', 'width', 'height', 'color' )