from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

#class Specialty(models.Model):
#    ID = models.CharField(max_length=50)

class  Doc_time(models.Model):
    user = models.OneToOneField(User , verbose_name="user",on_delete=models.CASCADE,null=True,blank=True)
    time = models.DateTimeField(verbose_name="appointments", auto_now=False, auto_now_add=False,null=True,blank=True)

    


category_choise= (('Dentistry','Dentistry'),
        ('Psychiatry','Psychiatry'),
        ('Neurology ','Neurology '),
        ('Ear, Nose and Throat','Ear, Nose and Throat'),
        ('Chest and Respiratory','Chest and Respiratory'),
        ('Heart','Heart'),
        ('Brain & Nerves','Brain & Nerves'),
        ('Bones','Bones'),
        (' Male Infertility',' Male Infertility'),
        ('Pediatrics and New Born','Pediatrics and New Born'),)


class Doctors_profile(models.Model):
    user = models.OneToOneField(User , verbose_name="user",on_delete=models.CASCADE)

    name=models.CharField(verbose_name="Name", max_length=50)

    E_mail = models.CharField(max_length=50, verbose_name='E-Mail')
    phone_number = models.CharField(max_length=11, verbose_name='Phone',default='')
    #phone_num =models.PhoneNumberField(null=False, blank=False, unique=True)
    location = models.CharField(max_length=50,verbose_name='Location')
    Specialty = models.CharField(max_length=50,verbose_name='Specialty', choices=category_choise,default='')     
    who_i=models.TextField( verbose_name="synopsis about your self", max_length=250)
    price=models.IntegerField( verbose_name="price")
    image=models.ImageField( verbose_name="Personal Image", upload_to='Doctors_profile', default='',blank=True)
    new_join=models.DateTimeField(verbose_name="joining_Time", auto_now_add=True)
    DocTime = models.ForeignKey(Doc_time, on_delete=models.CASCADE, verbose_name="Appointments ",null=True,blank=True)


    
    class Meta:
        verbose_name = ("Doctor_profile")
        verbose_name_plural = ("Doctors_profiles")

    def __str__(self):
        return self.name


#eng.zeyad instructions
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="v2")
#     def is_admin(self):
#         return self.user.is_superuser == 1


