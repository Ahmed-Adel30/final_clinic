from dataclasses import fields
from xml.parsers.expat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    
      class Meta:
        model = User
        fields = ("username","email","password1","password2")
        #fields: tuple[Literal['username'], Literal['email'], Literal['password1'], Literal['password2']]