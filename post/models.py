from django.db import models

# Create your models here.


IMAGE_FROM_CHOICES = (('upload' , 'upload') , ('url' , 'url'))
CROP_TYPE_CHOICES = (('corner' , 'corner') , ('center' , 'center'))
TITLE_TEXT_POSTION_CHOICES = (('top' , 'top') , ('center' , 'center') , ('bottom' , 'bottom'))
TITLE_TEXT_ALIGNMENT_CHOICES = (('justified' , 'justified') , ('center' , 'center')  , ('leftAlign' , 'leftAlign'))


class Post(models.Model):
    imageFrom = models.CharField(choices=IMAGE_FROM_CHOICES , max_length=100)
    title = models.CharField(max_length=200 )
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    imageURL = models.URLField()
    cropType =  models.CharField(choices=CROP_TYPE_CHOICES , max_length=100)
    isAddGradient = models.BooleanField(default=True)
    isAddBranding = models.BooleanField(default=True)
    isAddTitleText = models.BooleanField(default=True)
    titleTextPosition = models.CharField(choices=TITLE_TEXT_POSTION_CHOICES , max_length=100)
    titleTextAlignment = models.CharField(choices=TITLE_TEXT_ALIGNMENT_CHOICES , max_length=100)
    isContainImportantWords = models.BooleanField(default=True)
    savedFilename = models.CharField(max_length=100)








    def __str__(self):
        return self.title
