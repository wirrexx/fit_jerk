
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import FitUserForm, UserInfoForm


# Create your views here.

def index_view(request):
    return render()

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
            
            # send_confirmation_email()

            # Authenticicate and login the new user
            #NOTE: Is this step realy necessary?
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #   redirect to complete_your_profile view
                return redirect("complete_profile")
    else: 
        form = FitUserForm()
    return render(request, "registration/signup.html", {"form":form})

@login_required
def complete_profile(request):
    #TODO: Create CompleteProfileForm
    # if request.method = "GET":
    # show signup successfull message, welcome the user
    # show CompleteProfileForm
    # show link to Logout
    # show 

    if request.method == "POST":
        form = UserInfoForm(request.POST)
        # sanitize data
        # save data to database
        # redirect to index
        if form.is_valid():

            return redirect("profile")
    else:
        form = UserInfoForm()
    return render(request, "registration/complete_profile.html", {"form":form})

def profile_view(request):
    # if userinformation != complete:
    # show message: diggi, you forgot to 
    # show bmi
    # show workouts
    return render(request, "fitness_jerk/profile.html")

def password_reset_view(request):
    #TODO: Research password reset via email
    return render(request, "registration/passwd_reset.html")

def logout(request):
    pass

