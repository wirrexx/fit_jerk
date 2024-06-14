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


# Create your views here.

# ---------------------------------- XTIAN ---------------------------------------

## Password Reset
class CustomPasswordResetView(PasswordResetView):
    template_name = "registration/custom_password_reset_form.html"
    email_template_name = "registration/custom_password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/custom_password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/custom_password_reset_confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/custom_password_reset_complete.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "registration/change_password.html"


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/change_password_done.html"


class CustomLoginView(LoginView):
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

def delete_user_func(request):
    """Lets the user delete his profile"""
    username = request.user.username
    if request.method == 'POST':
        user_id = request.user.id
        user_to_delete = User.objects.filter(pk=user_id)
        user_to_delete.delete()
        return redirect('login')
    return render(request, "fitness_jerk/delete.html", {'member': username})


@login_required
def profile_view(request):
    user = request.user
    member_info = Members.objects.get(user=user)
    member_posts = Posts.objects.filter(member=member_info).last()
    BMI = user.members.bmi

    if BMI == 0:
        BMI = "Please complete your profile"

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
    """settings page where member can update and delete account"""
    user = request.user
    member_info = Members.objects.get(user=user)
    profile_form = ProfileChangeForm(request.POST or None, instance=member_info)
    profile_pic = PictureChangeForm(request.POST or None, request.FILES, instance=member_info)
    if profile_form.is_valid() and profile_pic.is_valid():
        profile_form.save()
        profile_pic.save()
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


def get_all_replies(path_to_response_file: str) -> list:
    """Returns content of a file as a list of strings one string per line"""
    try:
        with open(path_to_response_file) as f:
            content = f.readlines()
    except FileNotFoundError as err:
        print(err)
    return content    


@login_required
def workout_finish(request):
    """"""
    BASE_DIR = Path(__file__).resolve().parent 
    path_to_response_file = BASE_DIR / "templates/tough_responses.txt" 
    posts_list = get_all_replies(path_to_response_file) #TODO: Store this in a different way/generate GPT
    user = request.user
    member_info = Members.objects.get(user=user)
    msg = random.choice(posts_list)
    Posts.objects.create(member=member_info, post=msg)
    Members.objects.update(progress=(member_info.progress+1))
    return redirect('profile')


# ---------------------------------------- WISAM --------------------------------------

@login_required
def weight_loose(request):
    """"""
    exercises = [
        {'name': 'Squats', 'duration': 30},
        {'name': 'Pushups', 'duration': 30},
        {'name': 'Situps', 'duration': 30},
        {'name': 'Burpees', 'duration': 30},
        {'name': 'Mountain Climbers', 'duration': 30},
        {'name': 'Lunge Jumps', 'duration': 30},
        {'name': 'Plank', 'duration': 60},
        {'name': 'Punches non-stop', 'duration': 60},
        {'name': 'Climbers', 'duration': 30},
    ]
    training_schedules = TrainingSchedule.objects.all()
    return render(request, 'fitness_jerk/exercise_loose.html', {'exercises': exercises, 'training_schedules': training_schedules})




@login_required
def tone_down(request):
    """"""
    exercises = [
        {'name': 'Push Ups', 'duration': 1},
        # {'name': 'Plank', 'duration': 60},
        # {'name': 'Glute Bridge', 'duration': 30},
        # {'name': 'Jumping Jacks', 'duration': 60},
        # {'name': 'Side Lunges', 'duration': 30},
        # {'name': 'Lunges', 'duration': 30},
        # {'name': 'Chair Squat', 'duration': 30},
        # {'name': 'Sumo Squat Hammer Curl', 'duration': 30},
        # {'name': 'Triceps Extension', 'duration': 30},
    ]
    training_schedules = TrainingSchedule.objects.all()
    return render(request, 'fitness_jerk/exercise_tone.html', {'exercises': exercises, 'training_schedules': training_schedules})



@login_required
def build_muscles(request):
    """"""
    exercises = [
        {'name': 'Overhead Crunch', 'duration': 5},
        # {'name': 'Pistol Squat', 'duration': 30},
        # {'name': 'Dips', 'duration': 30},
        # {'name': 'Sit Ups', 'duration': 30},
        # {'name': 'Burpees', 'duration': 30},
        # {'name': 'Mountain Climbers', 'duration': 30},
        # {'name': 'Bench Dips', 'duration': 30},
        # {'name': 'Push Ups', 'duration': 30},
        # {'name': 'Plank', 'duration': 60},
        

    ]
    training_schedules = TrainingSchedule.objects.all()
    return render(request, 'fitness_jerk/exercise_muscles.html', {'exercises': exercises, 'training_schedules': training_schedules})




#---------------------Landing Page --------------------

class LandingPage(TemplateView):
    template_name = "fitness_jerk/landing_page.html"
    
class AboutPage(TemplateView):
    template_name = "fitness_jerk/learn_more.html"

