from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, DecimalValidator
from django.contrib.auth.password_validation import validate_password
from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from .models import Members

def validate_height(value):
    """THIS FUNCTION IS TO VALIDATE THE HIGHT FORMAT AS THE DEFAULT VALUE IS 0. I HAD TO ADD AN IF STATEMENT"""
    if value != 0:
        regex_validator = RegexValidator(
            regex=r'^\d{1}\.\d{2}$',
            message="Please enter in the correct format"
        )
        regex_validator(value)

class ProfileChangeForm(UserChangeForm):
    """FORM TO UPDATE THE HIGHT AND WEIGHT"""
    #hide password change message
    password = None
    class Meta:
        model = Members 
        fields = ['height', 'weight']
    
    height = forms.FloatField(
        required=False,
        error_messages={'invalid': 'Height format X.XX'},
        validators=[validate_height],
        widget=forms.NumberInput(attrs={'pattern': r'[0-9]{1}[.][0-9]{2}', 'title': 'Please add your height in the format X.XX'})
    )


class PictureChangeForm(forms.Form):
    """A SEPARATED FORM FOR THE PICTURE SO I COULD PLACE AT THE BOTTOM OF THE SETTINGS PAGE AND STYLE IT BETTER"""
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'title': 'Upload your picture', 'placeholder': 'Choose your file'}))
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
        #TODO: Rexex: " @*=#`´!|><" are not supposed to be in the username
        #   check if username is valid
        #       empty 
        #       with special characters
        #   check if username is taken
        if " " in self.cleaned_data.get("username"):
            raise ValidationError("Space in username")
        username = self.cleaned_data.get("username")
        
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username taken")
        return username              


    def clean_email(self):
        """Checks if email is valid"""
        email = self.cleaned_data.get("email")
        #   check if email is valid
        #   check if email is taken
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
    

