from django.urls import path 
from . import views

urlpatterns = [
    path('',views.my_views,name='registration'),
    path('register',views.register,name='register'),
    path('login',views.log,name='log'),
    path('LogOut',views.logout,name='LogOut'),
    path('LearnMore',views.lm,name='LearnMore'),
]