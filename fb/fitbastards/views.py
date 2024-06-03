from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members, Posts
from django.contrib.auth import authenticate, login, logout
from .forms import Profile, Profile_pic
from django import forms
from django.contrib import messages
from django.urls import reverse
import random

posts_list = ["ok", "done", "OMG", "finally"]
    
#this view is to simulate when the member logs in so the testing profile would get the member id
def login_test(request):
    members = Members.objects.all().values()
    template = loader.get_template("test.html")
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context, request))

#display for now the member profile info
def profile_test(request, id):
    data = Members.objects.get(id=id)
    member_posts = Posts.objects.filter(member=data)
    template = loader.get_template('profile.html')
    progress = data.progress/10*100
    
    if data.height and data.weight:
        BMI = data.weight/(data.height**2)
        
        context = {
            'member': data,
            'BMI': f"{BMI:.2f}",
            'progress': f"{progress:.0f}%",
            'posts': member_posts
            
        }

    else:
        BMI = "Please complete your profile"
    
        context = {
          'member': data,
          'BMI': BMI,
          'progress': f"{progress:.0f}%",
          'posts': member_posts
          
        }

    
    return HttpResponse(template.render(context, request))

#settings page where member can update and delete account
def settings(request, id):
    #this is to when we have the login implemented
    #if request.user.is_authenticated:
        #current_user = Members.objects.get(id=id)
    member = Members.objects.get(id=id)
    progress = member.progress/10*100
    profile_form = Profile(request.POST or None, instance=member)
    profile_pic = Profile_pic(request.POST or None, request.FILES, instance=member)
    
    if profile_form.is_valid() and profile_pic.is_valid():
        profile_form.save()
        profile_pic.save()
        messages.success(request, "Profile updated successfully")
       
        return redirect(reverse('details', kwargs={'id': id}))  
    
    if member.height and member.weight:
        BMI = member.weight/(member.height**2)
        
        context = {
            'member': member,
            'BMI': f"{BMI:.2f}",
            'progress': f"{progress:.0f}%"
        }

    else:
        BMI = "Please complete your profile"
    
        context = {
          'member': member,
          'BMI': BMI,
          'progress': f"{progress:.0f}%"
        } 

    return render(request, 'settings.html', {'profile_form': profile_form, 'profile_pic': profile_pic, 'context': context})
    

#logout func 
def member_logout(request):
    logout(request)
    return redirect('/')

def workout_finish(request, id):
    member = get_object_or_404(Members, id=id)
    msg = random.choice(posts_list)
    Posts.objects.create(member=member, post=msg)
    Members.objects.update(progress=(member.progress+1))
    
    return redirect(reverse('details', kwargs={'id': id}))

def delete(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('delete.html')
    context = {
      'member': member,
    }

    if request.method == 'POST':
        dmember = Members.objects.filter(pk=id)
        dmember.delete()

        return redirect('members')
    
    return HttpResponse(template.render(context, request))