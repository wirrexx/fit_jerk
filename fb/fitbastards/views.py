from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
    
#this view is to simulate when the member logs in so the testing profile would get the member id
def login_test(request):
    members = Members.objects.all().values()
    template = loader.get_template("test.html")
    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))

#display for now the member info and progress bar
def profile_test(request, id):
    data = Members.objects.get(id=id)
    template = loader.get_template('profile.html')
    BMI = data.weight/(data.height**2)
    progress = data.progress/10*100
    
    context = {
      'member': data,
      'BMI': f"{BMI:.2f}",
      'progress': f"{progress:.0f}%"
    }
    
    return HttpResponse(template.render(context, request))

