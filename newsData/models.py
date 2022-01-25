from django.db import models

# Create your models here.

class newsData(models.Model):

    title = models.CharField(max_length=200 )
    content = models.TextField()
    imageURL = models.URLField()

    
    def __str__(self):
        return self.title