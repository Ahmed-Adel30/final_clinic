from atexit import register
from django.contrib import admin
from .models import  payments


admin.site.register(payments)