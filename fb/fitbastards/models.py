from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#this model it's just for testing. To check and create the progress bar and calculate the BMI
#created the image field so member can upload image and update also

class Members(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    progress = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="static/")
    

class Posts(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    post = models.CharField(max_length=255, null=True)

class TrainingSchedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    
    def __str__(self):
        return self.title
    

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Duration in seconds")

    def __str__(self):
        return self.name

