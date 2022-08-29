from dataclasses import field
from django import forms
from . import models

class ConstructionForm(forms.ModelForm):
    class Meta:
        model = models.Construction
        fields = ['category', ]