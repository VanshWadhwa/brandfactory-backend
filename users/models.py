from tkinter.tix import Tree
from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from .storage import OverwriteStorage

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

class Profile(models.Model): 

    
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , related_name='profile')
  
    handleName = models.CharField(max_length=20, null = True , blank=True)
    primaryColor = models.CharField(max_length=7, default="#ffffff")
    secondaryColor = models.CharField(max_length=7, default="#1b9df0")
    logoImage = models.ImageField(default = 'defaultLogo.png' , storage=OverwriteStorage(), upload_to=lambda instance, filename: 'images/{0}/{1}'.format(instance.user.username, "logoImage.png"))
    tempImage1 = models.ImageField(default = 'tempImage1.png' ,storage=OverwriteStorage(), upload_to=lambda instance, filename: 'images/{0}/{1}'.format(instance.user.username, "tempImage1.png"))
    tempImage2 = models.ImageField(default = 'tempImage2.png' ,storage=OverwriteStorage(), upload_to=lambda instance, filename: 'images/{0}/{1}'.format(instance.user.username, "tempImage2.png"))
    tempImage3 = models.ImageField(default = 'tempImage3.png' ,storage=OverwriteStorage(), upload_to=lambda instance, filename: 'images/{0}/{1}'.format(instance.user.username, "tempImage3.png"))
    telegramToken = models.CharField(max_length=200, null = True , blank=True)


# Token
# Telegram token
    # image = models.ImageField(default = 'default.png' , upload_to = 'images/'+user.username)
  



    def __str__(self):
        return f'{self.user.username} Profile'
