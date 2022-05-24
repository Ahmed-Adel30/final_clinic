from django.urls import path 
from . import views

urlpatterns = [
    path('credit_card',views.pay,name='credit_card'),
    path('congrats',views.congrats,name='congrats'),
] 