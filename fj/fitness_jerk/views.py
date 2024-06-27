import random

from django.contrib import messages
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView, TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from pathlib import Path
from .forms import FitUserForm, ProfileChangeForm, PictureChangeForm
from .models import UserProfile, TrainingSchedule
from pathlib import Path
from .static import exercise_static

##TODO: 
#+  1. Refactor
#+  2. Add docstrings

# Create utilities here
def get_file_content_as_list(path_file: str) -> list:
    """Returns content of a file as a list of strings one string per line"""
    try:
        with open(path_file) as f:
            content = f.readlines()
    except FileNotFoundError as err:
        print(err)
    return content    


BASE_DIR = Path(__file__).resolve().parent 
RESPONSE_FILE = BASE_DIR / "templates/tough_responses.txt"
EXERCISES = exercise_static.EXERCISES



# ---------------------------------- XTIAN ---------------------------------------

## Password Reset
class CustomPasswordResetView(PasswordResetView):
    """Allows user to reset password if forgotten"""
    template_name = "registration/custom_password_reset_form.html"
    email_template_name = "registration/custom_password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """Informs the user if password reset was successfull"""
    template_name = "registration/custom_password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """This view uses a custom template to display the password reset confirmation form."""
    template_name = "registration/custom_password_reset_confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """This view uses a custom template to display the password reset completion message."""
    template_name = "registration/custom_password_reset_complete.html"


class CustomPasswordChangeView(PasswordChangeView):
    """This view uses a custom template to display the password change form."""
    template_name = "registration/change_password.html"


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    """This view uses a custom template to display the password change success message."""
    template_name = "registration/change_password_done.html"


class CustomLoginView(LoginView):
    """This view uses a custom template to display the login form."""
    template_name = "registration/login.html"

## Signup
def signup_view(request):
    """View that lets the user signup to the page. Sends a welcome mail upon successfull signup"""
    if request.method == "POST":
        form = FitUserForm(request.POST)
        if form.is_valid():  
            username = form.cleaned_data.get("username")                # create the new user
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user = User.objects.create_user(username=username, email=email, password=password)  
            user_profile = UserProfile.objects.create(user=user)               # create userinfo related to new user
            send_mail(                                                  # send welcome email to user
                subject=f"Welcome to FitBastard",
                message="You finally made it. You choose to better yourself. Well, good luck with that!",
                from_email="fitbastards.team@gmail.com",
                recipient_list=[email],
            )
            user.backend = "django.contrib.auth.backends.ModelBackend"  # Choose correct backend for user creation -> settings/AUTHENTICATION_BACKENDS
            login(request, user)    
            return redirect("profile")
        else:
            return render(request, "registration/signup.html", {"form":form})
    else: 
        form = FitUserForm()
    return render(request, "registration/signup.html", {"form":form})


#logout functionality
def logout_endpoint(request):
    """Logs out the user"""
    logout(request)
    return redirect('/')


# ------------------------------------- ANA ----------------------------------------

@login_required
def delete_user_func(request):
    """Let the user delete his profile"""
    username = request.user.username
    if request.method == 'POST':
        user_id = request.user.id
        user_to_delete = User.objects.filter(pk=user_id)
        user_to_delete.delete()
        return redirect('login')
    return render(request, "fitness_jerk/delete.html", {'member': username})


@login_required
def profile_view(request):
    """here the user information is displayed in the profile page and depending on the member's workouts number it recognizes his bastard level and calculate the percentage of that level progress"""
    user = request.user
    #user_profile = UserProfile.objects.get(user=user)
    latest_post =  user.userprofile.latest_post
    BMI = user.userprofile.bmi
    
    progress_percentage = user.userprofile.progress/90*100
    if BMI == 0:
        BMI = "Please complete your profile"
    
    context = {
        'member': user,
        'BMI': BMI,
        'progress': f"{progress_percentage:.0f}%",
        'motivational_msg': latest_post,
        'level': user.userprofile.level
    }
    return render(request, 'fitness_jerk/profile.html', context)

@login_required
def settings_view(request):
    """settings page where member can update and go to the delete account page"""
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    profile_form = ProfileChangeForm(request.POST or None, instance=user_profile)
    profile_pic = PictureChangeForm(request.POST or None, request.FILES)
    
    """THIS PART IS SO THE MEMBER CAN CHOOSE BETWEEN UPLOAD HIS OWN PICTURE OR GET AN AVATAR"""
    if request.method == 'POST':
        avatar = request.POST.get('avatar')  # Retrieve selected avatar option
        noimage = request.POST.get('noimage')

        if profile_form.is_valid() and profile_pic.is_valid():
            profile_form.save()
            
            image = profile_pic.cleaned_data['image']
            
            if noimage:
                user_profile.image = None # this is if the member want to change his profile to no picture after
                user_profile.save()

            if image:
                user_profile.image = image
                user_profile.save()
            
            """here the POST request get the avatar name and save the image accordingly"""
            if avatar:
                if avatar == 'batman':
                    user_profile.image = 'static/batman.jpeg'
                if avatar == 'catwoman':
                    user_profile.image = 'static/catwoman-lego.png'
                if avatar == 'superman':
                    user_profile.image = 'static/superman_lego.jpeg'
                if avatar == 'wonderwoman':
                    user_profile.image = 'static/wonderwoman_lego.jpg'    
                
                user_profile.save()

            messages.success(request, "Profile updated successfully")
            return redirect('profile')
        
    BMI = user.userprofile.bmi
    if BMI == 0:
        BMI = "Please complete your profile"

    context = {
        'member': user_profile,
        'BMI': BMI,
    } 
    return render(request, 'fitness_jerk/settings.html', {'profile_form': profile_form, 'profile_pic': profile_pic, 'context': context})


@login_required
def workout_finish(request):
    """once the member hit the button done in the workout page this function is triggered"""
    user = request.user
    member_info = user.userprofile
    member_info.progress += 1
    member_info.workouts_done += 1
    member_info.latest_post = random.choice(get_file_content_as_list(RESPONSE_FILE))
    if member_info.progress == 90:
        member_info.progress = 0
    member_info.save()
    return redirect('profile')

# ---------------------------------------- WISAM --------------------------------------


@login_required
def workout_view(request, exercise_type):
    exercise = EXERCISES[exercise_type]["exercise"]
    template = EXERCISES[exercise_type]["template"]
    training_schedules = TrainingSchedule.objects.all()
    return render(request, template, {'exercises': exercise, 'training_schedules': training_schedules})


#---------------------Landing Page --------------------

class LandingPage(TemplateView):
    template_name = "fitness_jerk/landing_page.html"

class AboutPage(TemplateView):
    template_name = "fitness_jerk/learn_more.html"

class ImprintView(TemplateView):
    template_name = "fitness_jerk/imprint.html"

class PrivacyPolicyView(TemplateView):
    template_name = "fitness_jerk/privacy_policy.html"

