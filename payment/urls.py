from django.urls import path 
from . import views

urlpatterns = [
    path('credit_card',views.pay,name='credit_card'),
    path('congrats',views.congrats,name='congrats'),
    path('update/<int:id>',views.update,name='update'),
    path('conformation',views.conformation,name='conformation'),
    path('delete/<int:id>',views.delete,name='delete'),



] 