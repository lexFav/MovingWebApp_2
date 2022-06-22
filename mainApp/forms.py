import imp
from django import forms
from django.forms import ModelForm
from .models import Box, BoxItem

class BoxForm(ModelForm):
    class Meta:
        model = Box
        fields = ('box_number', 'box_description', 'box_location')
        labels = {
            'box_number': 'Number',
            'box_description': 'Description',
            'box_location': 'Location',
        }
        widgets = {
            'box_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Box Number'}),
            'box_description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Box Description'}),
            'box_location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Box Location'}),
        }

class BoxItemForm(ModelForm):
    class Meta:
        model = BoxItem
        fields = ('box', 'item_name', 'item_quantity')
        labels = {
            'box': 'Box Number',
            'item_name': 'Item Name',
            'item_quantity': 'Item Quantity',
        }
        widgets = {
            'box': forms.Select(attrs={'class':'form-control', 'placeholder':'Box Number'}),
            'item_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Name'}),
            'item_quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Quantity'}),
        }