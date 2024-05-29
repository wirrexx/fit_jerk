from django.contrib.auth.models import User
from django.db import models

#TODO: Write __str__ for UserInfo

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_weight = models.FloatField(default=None)
    user_height = models.FloatField(default=None)

