import random
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .forms import FitUserForm, UserInfoForm, ProfileChangeForm, PictureChangeForm
from .models import Profile, Posts


# Create your views here.

#display for now the member profile info
def profile_test(request, id):
    user = User.objects.get(id=id)
    member_posts = Posts.objects.filter(member=id)
    template = loader.get_template('fitness_jerk/profile.html')
    progress = user.profile.progress/10*100
    
    if user.profile.height and user.profile.weight:
        BMI = user.profile.weight/(user.profile.height**2)
        
        context = {
            'member': user,
            'BMI': f"{BMI:.2f}",
            'progress': f"{progress:.0f}%",
            'posts': member_posts 
        }

    else:
        BMI = "Please complete your profile"
    
        context = {
          'member': user,
          'BMI': BMI,
          'progress': f"{progress:.0f}%",
          'posts': member_posts
        }
    return HttpResponse(template.render(context, request))


def delete_user_func(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user_to_delete = User.objects.filter(pk=id)
        user_to_delete.delete()
        return redirect('login')
    return render(request, "fitness_jerk/delete.html", {'member': user})


def send_confirmation_email():
    subject = "Signup confirmation"
    message = ""
    from_email = ""

def signup_view(request):
    if request.method == "POST":
        form = FitUserForm(request.POST)
        
        # is_valid executes cleaning functions defined in forms 
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


def profile_view(request):
    user = request.user
    
    # if userinformation != complete:
    # show message: diggi, you forgot to 
    # show bmi
    # show workouts
    return render(request, "fitness_jerk/profile.html")

# def login_func(request, user):
#     if request.method == "POST":
#         login(request, user)
#     pass

def password_reset_view(request):
    #TODO: Research password reset via email
    return render(request, "registration/passwd_reset.html")

#logout func 
def logout_endpoint(request):
    """Logs out the user"""
    logout(request)
    return redirect('/')


def workout_finish(request, id):
    """"""
    posts_list = ["ok", "done", "OMG", "finally"]
    member = get_object_or_404(UserInfo, id=id)
    msg = random.choice(posts_list)
    Posts.objects.create(member=member, post=msg)
    Profile.objects.update(progress=(member.progress+1))
    return redirect(reverse('details', kwargs={'id': id}))

#settings page where member can update and delete account
def settings_view(request, id):
    """"""
    #this is to when we have the login implemented
    #if request.user.is_authenticated:
        #current_user = Members.objects.get(id=id)
    user = User.objects.get(id=id)
    progress = user.profile.progress/10*100
    
    profile_form = ProfileChangeForm(request.POST or None, instance=user)
    profile_pic = PictureChangeForm(request.POST or None, request.FILES, instance=user)
    
    if profile_form.is_valid() and profile_pic.is_valid():
        profile_form.save()
        profile_pic.save()
        messages.success(request, "Profile updated successfully")
       
        return redirect(reverse('details', kwargs={'id': id}))  
    
    if user.profile.height and user.profile.weight:
        BMI = user.profile.weight/(user.profile.height**2)
        BMI = f"{BMI:.2f}"
    else:
        BMI = "Please complete your profile"
    context = {
        'member': user,
        'BMI': BMI,
        'progress': f"{progress:.0f}%"
    } 
    return render(request, 'fitness_jerk/settings.html', {'profile_form': profile_form, 'profile_pic': profile_pic, 'context': context})
    