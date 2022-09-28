from django import forms
from django.forms import ModelForm
from . import models

#creating Construction form
class ConstructionForm(forms.ModelForm):
    class Meta:
        model = models.Construction
        fields = ('category', 'reference_name', 'width', 'height', 'color' )
        
        labels = {
            'project': "PROJECT",
            'category': "CATEGORY",
            'reference_name': "REFERENCE",
            'width': "WIDTH",
            'height': "HEIGHT",
            'color': "COLOR",
        }

        widgets = {
            'project': forms.Select(attrs={'class': 'form-control','readonly':'readonly'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'reference_name': forms.TextInput(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('user', 'name')
        
        labels = {
            'user': "USER",
            'name': "PROJECT REFERENCE NAME",
        }

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control '}),
            'name': forms.TextInput(attrs={'class': 'form-control '}),
        }