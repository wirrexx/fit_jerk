from django.db import models

# Create your models here.

#this model it's just for testing. To check and create the progress bar and calculate the BMI

class Members(models.Model):
    username = models.CharField(max_length=255)
    weight = models.FloatField()
    height = models.FloatField()
    progress = models.IntegerField()
