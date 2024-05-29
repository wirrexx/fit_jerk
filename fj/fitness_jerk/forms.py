from django import forms
from django.contrib.auth.forms import UserCreationForm

class FitBastardUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        help_text="Please enter a valid email"
    )
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data(["email"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user