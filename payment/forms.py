from django import forms
from .models import payments


class PaymentForm(forms.ModelForm):
  class Meta:
    model = payments 
    fields =[  #'__all__'
      'name',
      'cardNum',
      'epxpirationDate',
      'securityCode'
      ] 
    widgets={
      'epxpirationDate':forms.DateInput(format='%d-%m-%Y',  attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              })
    } 
      
                               

  

   