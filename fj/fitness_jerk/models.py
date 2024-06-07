from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

#TODO: Write __str__ for UserInfo

# Create your models here.
class Members(models.Model):
    """Representation of the secondary attributes of a User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    progress = models.IntegerField(default=0)
    
    # TODO:ImageField Path: It's generally not a good practice to upload user files to the static/ directory. It's better to use a directory like media/ for user-uploaded files and configure your project to serve them properly.
    image = models.ImageField(null=True, blank=True, upload_to="static/")

    def calculate_BMI(self):
        """calculates the users BMI"""
        if self.height > 0:
            return round(self.weight / (self.height ** 2), 2)
        return 0
    
    @property
    def bmi(self):
        return self.calculate_BMI()

## TODO: Investigate!
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Members.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.members.save()


class Posts(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
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
    