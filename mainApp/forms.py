import imp
from django import forms
from django.forms import ModelForm
from .models import Box, BoxItem

class BoxForm(ModelForm):
    class Meta:
        model = Box
        fields = ()
        labels = {
            
        }
        widgets = {

        }

class BoxItemForm(ModelForm):
    class Meta:
        model = BoxItem
        fields = ()
        labels = {

        }
        widgets = {
            
        }