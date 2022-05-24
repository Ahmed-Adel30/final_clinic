from django.urls import path 
from . import views

urlpatterns = [
    path('credit',views.pay,name='credit'),
]