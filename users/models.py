
from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from .storage import OverwriteStorage


class CustomUser(AbstractUser):
    def __str__(self):
        return self.email


def saveLogoImage(instance, filename):
    url = 'images/{0[0]}/{0[1]}'
    vars_array = [instance.user.username, "defaultLogo.png"]
    return url.format(vars_array)


def saveTempImage1(instance, filename):
    url = 'images/{0[0]}/{0[1]}'
    vars_array = [instance.user.username, "tempImage1.png"]
    return url.format(vars_array)


def saveTempImage2(instance, filename):
    url = 'images/{0[0]}/{0[1]}'
    vars_array = [instance.user.username, "tempImage2.png"]
    return url.format(vars_array)


def saveTempImage3(instance, filename):
    url = 'images/{0[0]}/{0[1]}'
    vars_array = [instance.user.username, "tempImage3.png"]
    return url.format(vars_array)


class Profile(models.Model):

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')

    handleName = models.CharField(max_length=20, null=True, blank=True)
    primaryColor = models.CharField(max_length=7, default="#ffffff")
    secondaryColor = models.CharField(max_length=7, default="#1b9df0")
    logoImage = models.ImageField(
        default='defaultLogo.png' ,  upload_to=saveLogoImage)
    tempImage1 = models.ImageField(
        default='tempImage1.png' ,  upload_to=saveTempImage1)
    tempImage2 = models.ImageField(
        default='tempImage2.png' ,  upload_to=saveTempImage2)
    tempImage3 = models.ImageField(
        default='tempImage3.png' ,  upload_to=saveTempImage3)
    telegramToken = models.CharField(max_length=200, null=True, blank=True)


# Token
# Telegram token
    # image = models.ImageField(default = 'default.png' , upload_to = 'images/'+user.username)


    def __str__(self):
        return f'{self.user.username} Profile'
