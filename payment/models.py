from pickle import TRUE
from django.contrib.auth.models import User
from django.db import models

class Payment(models.Model):
    name=models.CharField(verbose_name="name", max_length=50,null=True,blank=True)
    cardNum=models.CharField(verbose_name="card number", max_length=16,null=True,blank=True)
    epxpirationDate=models.DateField(verbose_name="Expiration Date", auto_now=False, auto_now_add=False,null=True,blank=True)
    securityCode=models.CharField(verbose_name="security Code", max_length=3,null=True,blank=True)
    user = models.OneToOneField(User , verbose_name="user",on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
      return self.name
