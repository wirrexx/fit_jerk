from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

#TODO: Write string representation
# Create your models here.
class UserProfile(models.Model):
    """Representation of the secondary attributes of a User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    progress = models.IntegerField(default=0)
    workouts_done = models.IntegerField(default=0)
    level = models.CharField(default="Newbie Bastard", max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="static/")

    def calculate_BMI(self):
        """calculates the users BMI"""
        if self.height > 0 and self.weight > 0:
            return round(self.weight / (self.height ** 2), 2)
        return 0
    
    def progress_percentage(self):
        """calculates the percentage of completion of the member's level"""
        pass

    def determine_user_level(self):
        """Determines the current level of a user: Newbie -> God Bastard"""
        level = "Newbie Bastard"
        if self.workouts_done < 90:
            level = "Newbie Bastard"
        elif 90 <= self.workouts_done < 180:
            level = "Fit Bastard"
        elif 180 <= self.workouts_done < 270:
            level = "Master Bastard"
        elif 270 <= self.workouts_done < 360:
            level = "Supreme Bastard"
        elif 360 <= self.workouts_done < 450:
            level = "Ultra Bastard"
        elif self.workouts_done >= 450:
            level = "God Bastard"
        return level

    @property
    def bmi(self):
        return self.calculate_BMI()
    
    @property
    def level(self):
        return self.determine_user_level()



class Posts(models.Model):
    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    post = models.CharField(max_length=255, default="Welcome")


# timer needs datetime 
class TrainingSchedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    
    def __str__(self):
        return self.title
    