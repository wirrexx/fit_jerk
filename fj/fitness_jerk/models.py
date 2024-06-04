from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

#TODO: Write __str__ for UserInfo

# Create your models here.
class Profile(models.Model):
    """Representation of the secondary attributes of a User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    progress = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="static/")

## TODO: Investigate!
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Posts(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.CharField(max_length=255, default="Welcome")