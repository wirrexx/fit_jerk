
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import FitBastardUserCreationForm
from django.http import HttpResponse

# Create your views here.
def test_form_view(request):
    if request.method == "POST":
        form = FitBastardUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("testendpoint")
    else:
        context = {"form":FitBastardUserCreationForm()}

    return render(request, "fitness_jerk/testform.html", context)

def test_endpoint(request):
    return HttpResponse("Thanks a bunch")

def signup_view(request):
    # TODO: Create UserCreationForm
    # if request.method == "GET":
    #   show SignupForm
    # if request.method == "POST"
    #   check if password meets requirements
    #   check if passwords match
    #   check if email is valid
    #   check if email is taken
    #   check if username is valid
    #   check if username is taken
    #   save user
    #   send confirmation email 
    #   log user in
    #   redirect to complete_your_profile view
    
    return render(request, "registration/signup.html")

@login_required
def complete_profile(request):
    #TODO: Create CompleteProfileForm
    # if request.method = "GET":
    # show signup successfull message, welcome the user
    # show CompleteProfileForm
    # show link to Logout
    # show 

    # if request.method == "POST":
    # sanitize data
    # save data to database
    # redirect to index
    return render(request, "registration/complete_profile.html")

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

