from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Project,Profile
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Project.display_images()
    date = dt.date.today()   
  
    return render(request, 'photos/index.html', {"images":images,"date": date,})

@login_required
def profile(request):
    fo=Profile.pro()
    # profile=Profile.objects.get(id=id)
    # current_profile=Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {"fo":fo,"profile":profile})