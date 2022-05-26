from dataclasses import field
from django import forms
from .models import Doc_time

class Doc_timeForm(forms.ModelForm):
    class Meta:
        model = Doc_time
        fields = ["time"]
        widgets={
       'time':forms.Select()
    } 
