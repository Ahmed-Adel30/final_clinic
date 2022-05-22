import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class DoctorsFilter(django_filters.FilterSet):
    class Meta:
        model = Doctors_profile
        fields  = '__all__'
        exclude = ['price','user','who_i','E_mail','phone_number' ,'image','new_join']