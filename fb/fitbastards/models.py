from django.db import models

# Create your models here.

#this model it's just for testing. To check and create the progress bar and calculate the BMI
#created the image field so member can upload image and update also

class Members(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    progress = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="static/")
    

class Posts(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    post = models.CharField(max_length=255, default="Welcome")
