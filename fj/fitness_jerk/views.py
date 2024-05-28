from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index_view(request):
    return render(request, "fitness_jerk/index.html")
