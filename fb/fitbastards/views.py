from django.shortcuts import render, redirect, get_object_or_404
from .models import Members, Posts, TrainingSchedule
from django.contrib.auth import logout, login
from .forms import Profile, Profile_pic, FitUserForm, UserInfoForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random 
from django.core.mail import send_mail


posts_list = ["ok", "done", "OMG", "finally"] #TODO STORE THIS IN A JSON.FILE

def signup_view(request):

    if request.method == "POST":
        form_user = FitUserForm(request.POST)
        
        # is_valid executes cleaning functions defined in forms 
        if form_user.is_valid():
            # create the new user
            username = form_user.cleaned_data.get("username")
            password = form_user.cleaned_data.get("password1")
            email = form_user.cleaned_data.get("email")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            
            send_mail(
                subject=f"Welcome to FitBastard",
                message="You finally made it. You choose to better yourself. Well, good luck with that!",
                from_email="fitbastards.team@gmail.com",
                recipient_list=[email],
            ) 

            login(request, user)
            new_user = request.user
            
            member = Members.objects.create(username=new_user)
            member.save()

            return redirect("details")
    
    else: 
        form_user = FitUserForm()
    return render(request, "signin.html", {"form_user": form_user})  


def password_reset_view(request):
    #TODO: Research password reset via email
    return render(request, "pass_reset.html")

#TODO CREATE THE PROGRESS LEVELS 
@login_required
def profile_view(request):
    user = request.user
    
    member_info = Members.objects.get(username=user)
    member_posts = Posts.objects.filter(member=member_info)
    progress = member_info.progress/10*100

    if member_info.height and member_info.weight:
        BMI = member_info.weight/(member_info.height**2)
    
        context = {
            'member': member_info,
            'BMI': f"{BMI:.2f}",
            'progress': f"{progress:.0f}%",
            'posts': member_posts
        
        }
    
    else:

        BMI = "Please complete your profile"

        context = {
          'member': member_info,
          'BMI': BMI,
          'progress': f"{progress:.0f}%",
          'posts': member_posts
      
        }

    return render(request, 'profile.html', context)


@login_required
def settings_view(request):
    """settings page where member can update and delete account"""
    #TODO DISPLAY THE MEMBER LEVEL 
    user = request.user
    
    member_info = Members.objects.get(username=user)
    progress = member_info.progress/10*100

    
    profile_form = Profile(request.POST or None, instance=member_info)
    profile_pic = Profile_pic(request.POST or None, request.FILES, instance=member_info)
    
    #IT'S NOT SAVING

    if profile_form.is_valid() and profile_pic.is_valid():
        profile_form.save()
        profile_pic.save()
        messages.success(request, "Profile updated successfully")
       
        return redirect('details')
    
    if member_info.height and member_info.weight:
        BMI = member_info.weight/(member_info.height**2)
        BMI = f"{BMI:.2f}"
    else:
        BMI = "Please complete your profile"

    context = {
        'member': member_info,
        'BMI': BMI,
        'progress': f"{progress:.0f}%"
    } 

    return render(request, 'settings.html', {'profile_form': profile_form, 'profile_pic': profile_pic, 'context': context})
    


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def workout_finish(request):
    user = request.user
    id = user.id
    member_info = Members.objects.get(username=user)
    msg = random.choice(posts_list)

    Posts.objects.create(member=member_info, post=msg)
    Members.objects.update(progress=(member_info.progress+1))
    
    return redirect('details')

def delete_view(request, id):
    user = request.user
    member = User.objects.get(id=id)

    if request.method == 'POST':
        member.delete()

        return redirect('login')
    return render(request, 'delete.html')

def weight_loose(request):
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
    return render(request, 'exercise_loose.html', {'exercises': exercises, 'training_schedules': training_schedules})



def tone_down(request):
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
    return render(request, 'exercise_tone.html', {'exercises': exercises, 'training_schedules': training_schedules})




def build_muscles(request):
    exercises = [
        {'name': 'Overhead Crunch', 'duration': 1},
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
    return render(request, 'exercise_muscles.html', {'exercises': exercises, 'training_schedules': training_schedules})