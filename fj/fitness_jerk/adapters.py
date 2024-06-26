from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from fitness_jerk.models import UserProfile  # Replace with your actual profile model

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        
        # Create the profile instance if it doesn't exist
        if not UserProfile.objects.filter(user=user).exists():
            UserProfile.objects.create(user=user)
        
        return user