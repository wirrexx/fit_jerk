import random
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
# from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse_lazy
from .forms import FitUserForm, ProfileChangeForm, PictureChangeForm
from .models import Members, Posts, TrainingSchedule


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

#login view
def login_view(request):
    pass

def index_view(request):
    return render(request, "fitness_jerk/index.html")


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


#TODO FIGURE IT OUT HOW TO ACCESS AND RETRIEVE INFO
@login_required
def profile_view(request):
    user = request.user
    member_info = Members.objects.get(user=user)
    member_posts = Posts.objects.filter(member=member_info)
    progress = member_info.progress/10*100
    BMI = user.members.bmi
    if BMI == 0:
        BMI = "Please complete your profile"
    context = {
        'member': member_info,
        'BMI': BMI,
        'progress': f"{progress:.0f}%",
        'posts': member_posts
    }
    return render(request, 'fitness_jerk/profile.html', context)

@login_required
def settings_view(request):
    """settings page where member can update and delete account"""
    user = request.user
    member_info = Members.objects.get(user=user)
    progress = member_info.progress/10*100
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
        'progress': f"{progress:.0f}%"
    } 
    return render(request, 'fitness_jerk/settings.html', {'profile_form': profile_form, 'profile_pic': profile_pic, 'context': context})
    

@login_required
def workout_finish(request):
    """"""
    posts_list = ["ok", "done", "OMG", "finally"] #TODO: Store this in a different way/generate GPT
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
        {'name': 'Squats', 'duration': 15},
        # {'name': 'Pushups', 'duration': 30},
        # {'name': 'Situps', 'duration': 30},
        # {'name': 'Burpees', 'duration': 30},
        # {'name': 'Mountain Climbers', 'duration': 30},
        # {'name': 'Lunge Jumps', 'duration': 30},
        # {'name': 'Plank', 'duration': 60},
        # {'name': 'Punches non-stop', 'duration': 60},
        # {'name': 'Climbers', 'duration': 30},
    ]
    training_schedules = TrainingSchedule.objects.all()
    return render(request, 'fitness_jerk/exercise_loose.html', {'exercises': exercises, 'training_schedules': training_schedules})




@login_required
def tone_down(request):
    """"""
    exercises = [
        {'name': 'Push Ups', 'duration': 30},
        {'name': 'Plank', 'duration': 60},
        {'name': 'Glute Bridge', 'duration': 30},
        {'name': 'Jumping Jacks', 'duration': 60},
        {'name': 'Side Lunges', 'duration': 30},
        {'name': 'Lunges', 'duration': 30},
        {'name': 'Chair Squat', 'duration': 30},
        {'name': 'Sumo Squat Hammer Curl', 'duration': 30},
        {'name': 'Triceps Extension', 'duration': 30},
    ]
    training_schedules = TrainingSchedule.objects.all()
    return render(request, 'fitness_jerk/exercise_tone.html', {'exercises': exercises, 'training_schedules': training_schedules})



@login_required
def build_muscles(request):
    """"""
    exercises = [
        {'name': 'Overhead Crunch', 'duration': 10},
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

