import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView, TemplateView
# from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse_lazy
from pathlib import Path
from .forms import FitUserForm, ProfileChangeForm, PictureChangeForm
from .models import Members, Posts, TrainingSchedule
from pathlib import Path
from .static import exercise_static

##TODO: 
#+  1. Refactor
#+  2. Add docstrings

# Create Constants here
BASE_DIR = Path(__file__).resolve().parent 
RESPONSE_FILE = BASE_DIR / "templates/tough_responses.txt"
EXERCISES = exercise_static.EXERCISES


# Create your views here.
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
    """"""
    template_name = "registration/custom_password_reset_confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """"""
    template_name = "registration/custom_password_reset_complete.html"


class CustomPasswordChangeView(PasswordChangeView):
    """"""
    template_name = "registration/change_password.html"


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    """"""
    template_name = "registration/change_password_done.html"


class CustomLoginView(LoginView):
    """"""
    template_name = "registration/login.html"

## Signup
def signup_view(request):
    """View that lets the user signup to the page. Sends a welcome mail upon successfull signup"""
    if request.method == "POST":
        form = FitUserForm(request.POST)
        if form.is_valid():
            # create the new user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user = User.objects.create_user(username=username, email=email, password=password)
            # send welcome email
            send_mail(
                subject=f"Welcome to FitBastard",
                message="You finally made it. You choose to better yourself. Well, good luck with that!",
                from_email="fitbastards.team@gmail.com",
                recipient_list=[email],
            )
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return redirect("profile")
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
    member_info = Members.objects.get(user=user)
    member_posts = Posts.objects.filter(member=member_info).last()
    BMI = user.members.bmi

    if BMI == 0:
        BMI = "Please complete your profile"

    #TODO: Think of a smarter way to store this to make the code more readable
    if member_info.progress < 50:
        level = "Newbie Bastard"
        progress = member_info.progress/50*100

    elif 50 <= member_info.progress < 100:
        level = "Fit Bastard"
        progress = (member_info.progress-50)/50*100

    elif 100 <= member_info.progress < 150:
        level = "Master Bastard"
        progress = (member_info.progress-100)/50*100

    elif 150 <= member_info.progress < 200:
        level = "Supreme Bastard"
        progress = (member_info.progress-150)/50*100

    elif 200 <= member_info.progress < 250:
        level = "God Bastard"
        progress = (member_info.progress-200)/50*100

    context = {
        'member': member_info,
        'BMI': BMI,
        'progress': f"{progress:.0f}%",
        'posts': member_posts,
        'level': level
    }
    return render(request, 'fitness_jerk/profile.html', context)

@login_required
def settings_view(request):
    """settings page where member can update and go to the delete account page"""
    user = request.user
    member_info = Members.objects.get(user=user)
    profile_form = ProfileChangeForm(request.POST or None, instance=member_info)
    profile_pic = PictureChangeForm(request.POST or None, request.FILES)
    
    """THIS PART IS SO THE MEMBER CAN CHOOSE BETWEEN UPLOAD HIS OWN PICTURE OR GET AN AVATAR"""
    if request.method == 'POST':
        avatar = request.POST.get('avatar')  # Retrieve selected avatar option
        noimage = request.POST.get('noimage')

        if profile_form.is_valid() and profile_pic.is_valid():
            profile_form.save()
            image = profile_pic.cleaned_data['image']

            if noimage:
                member_info.image = None # this is if the member want to change his profile to no picture after
                member_info.save()

            if image:
                member_info.image = image
                member_info.save()
            
            """here the POST request get the avatar name and save the image accordingly"""
            if avatar:
                if avatar == 'batman':
                    member_info.image = 'static/batman.jpeg'
                if avatar == 'catwoman':
                    member_info.image = 'static/catwoman-lego.png'
                if avatar == 'superman':
                    member_info.image = 'static/superman_lego.jpeg'
                if avatar == 'wonderwoman':
                    member_info.image = 'static/wonderwoman_lego.jpg'
                 
                member_info.save()

            messages.success(request, "Profile updated successfully")
            return redirect('profile')
        

    BMI = user.members.bmi
    if BMI == 0:
        BMI = "Please complete your profile"
    
    context = {
        'member': member_info,
        'BMI': BMI,
    } 
    return render(request, 'fitness_jerk/settings.html', {'profile_form': profile_form, 'profile_pic': profile_pic, 'context': context})


#TODO: rename
def get_all_replies(path_to_response_file: str) -> list:
    """Returns content of a file as a list of strings one string per line"""
    try:
        with open(path_to_response_file) as f:
            content = f.readlines()
    except FileNotFoundError as err:
        print(err)
    return content    


#TODO: BASE_DIR and path to response file are constants that can be defined at the beginning of views.py
@login_required
def workout_finish(request):
    """once the member hit the button done in the workout page this function is triggered"""
    posts_list = get_all_replies(RESPONSE_FILE) 
    user = request.user
    member_info = Members.objects.get(user=user)
    msg = random.choice(posts_list)
    Posts.objects.create(member=member_info, post=msg)
    Members.objects.update(progress=(member_info.progress+1))
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

