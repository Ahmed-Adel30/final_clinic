import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class DoctorsFilter(django_filters.FilterSet):
    class Meta:
        model = Doctors_profile
        fields  = ['Specialty']