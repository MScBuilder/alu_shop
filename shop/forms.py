from django import forms
from django.forms import ModelForm
from . import models

#creating Construction form
class ConstructionForm(forms.ModelForm):
    class Meta:
        model = models.Construction
        fields = ('category', 'reference_name', 'width', 'height', 'color', 'price' )
        
        labels = {
            'category': "CATEGORY",
            'reference_name': "REFERENCE",
            'width': "WIDTH",
            'height': "HEIGHT",
            'color': "COLOR",
            'price': "PRICE",
        }

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control container-sm'}),
            'reference_name': forms.TextInput(attrs={'class': 'form-control container-sm'}),
            'width': forms.NumberInput(attrs={'class': 'form-control container-sm'}),
            'height': forms.NumberInput(attrs={'class': 'form-control container-sm'}),
            'color': forms.TextInput(attrs={'class': 'form-control container-sm'}),
            'price': forms.NumberInput(attrs={'class': 'form-control container-sm'})
        }