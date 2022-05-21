from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
from matplotlib import image
# Create your models here.

#class Specialty(models.Model):
#    ID = models.CharField(max_length=50)
    
class Doctor(models.Model):
    x= [
        ('Dentistry','Dentistry'),
        ('Psychiatry','Psychiatry'),
        ('Neurology ','Neurology '),
        ('Ear, Nose and Throat','Ear, Nose and Throat'),
        ('Chest and Respiratory','Chest and Respiratory'),
        ('Heart','Heart'),
        ('Brain & Nerves','Brain & Nerves'),
        ('Bones','Bones'),
        (' Male Infertility',' Male Infertility'),
        ('Pediatrics and New Born','Pediatrics and New Born'),
    ]
    
    FirstName = models.CharField(max_length=50, verbose_name='First Name')
    LastName = models.CharField(max_length=50, verbose_name='Last Name')
    E_mail = models.CharField(max_length=50, verbose_name='E-Mail')
    phonenum = models.DecimalField(max_length=50,verbose_name='Phone Number')
    Specialty = models.CharField(max_length=50,verbose_name='Specialty', choices=x)     
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=50,verbose_name='Fees', default='$')
    image = models.ImageField(upload_to ='photos')
    
    
    
     
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="v2")


#     def is_admin(self):
#         return self.user.is_superuser == 1

