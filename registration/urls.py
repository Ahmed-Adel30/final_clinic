from django.urls import path 
from . import views

urlpatterns = [
    path('',views.my_views,name='registration'),
    path('register',views.register,name='register'),
    path('login',views.log,name='log'),
    path('try',views.try_temp,name='try'),
]