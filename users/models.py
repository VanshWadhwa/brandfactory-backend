from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
import os

class CustomUser(AbstractUser):

    # Any extra fields would go here

#     Name
# Email
# Password
# Logo
# handleName
# Temp1image
# Temp2image
# Temp3image
# Primary color
# Secondary color
# Token
# Telegram token

    # hexcolor = models.CharField(max_length=7, default="#ffffff")


    def __str__(self):
        return self.email

class Profile(models.Model): 

 
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , related_name='profile')
    # image = models.ImageField(default = 'default.jpg' , upload_to = 'images/'+user.username)
    image = models.ImageField(default = 'default.jpg' ,upload_to=lambda instance, filename: 'images/{0}/{1}'.format(instance.user.username, "temp1.png"))
    primaryColor = models.CharField(max_length=7, default="#00ff00")
    secondaryColor = models.CharField(max_length=7, default="#ff0000")



    def __str__(self):
        return f'{self.user.username} Profile'
