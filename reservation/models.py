from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="v2")

#     location = models.CharField(max_length=50)

#     def is_admin(self):
#         return self.user.is_superuser == 1