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