from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
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
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg' , upload_to = 'profile_pics')
    primaryColor = models.CharField(max_length=7, default="#00ff00")
    secondaryColor = models.CharField(max_length=7, default="#ff0000")


    def __str__(self):
        return f'{self.user.username} Profile'
