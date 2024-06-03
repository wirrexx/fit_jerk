from .models import Members
from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm


class Profile(UserChangeForm):
    #hide password change message
    password = None
    class Meta:
        model = Members
        fields = ['height', 'weight']

class Profile_pic(UserChangeForm):
    #hide password change message
    password = None
    image = forms.ImageField()
    class Meta:
        model = Members
        fields = ['image']
        


