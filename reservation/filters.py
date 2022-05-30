import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class DoctorsFilter(django_filters.FilterSet):
    name= django_filters.CharFilter(lookup_expr='icontains')
    location= django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Doctors_profile
        fields  = '__all__'
        exclude = ['DocTime','price','user','who_i','E_mail','phone_number' ,'image','new_join']