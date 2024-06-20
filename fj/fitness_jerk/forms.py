from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from .models import Members

class ProfileChangeForm(UserChangeForm):
    #hide password change message
    password = None
    class Meta:
        model = Members 
        fields = ['height', 'weight']

class PictureChangeForm(UserChangeForm):
    #hide password change message
    password = None
    class Meta:
        model = Members
        fields = ['image']
    


class FitUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    
    class Meta:    
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        """Checks if username is: empty, invalid or already exists and if so, raises ValidationError"""
        username = self.cleaned_data.get("username")
        
        # Check if username is empty
        if username == None:
            raise ValidationError("Username cannot be empty")
        
        # Check for special characters
        forbidden_chars = ["[","!","@","#","$","%","^","&","*","(", ")",",",",",".","?","\\",":","{","}","|","<",">","/","'","\""]
        for forbidden_char in forbidden_chars:
            if forbidden_char in username:
                raise ValidationError("Username can't contain special characters")
        
        # Check if username is taken
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken")
        return username              


    def clean_email(self):
        """Checks if email is valid"""
        email = self.cleaned_data.get("email")
        # Check if email is already taken
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already taken") 
        return email
    
    def clean_password1(self):
        """Checks if password meets requirements"""
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)
        return password1

    def clean_password2(self):
        """Checks if both passwords exist and match"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
    

