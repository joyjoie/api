from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Project,Profile
from . forms import ProfileUpdateForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Project.display_images()
    date = dt.date.today()   
  
    return render(request, 'photos/index.html', {"images":images,"date": date,})

@login_required
def profile(request):
    fo=Profile.pro()
    if request.method == 'POST':
       
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile/profile.html', {"fo":fo,"profile":profile,"p_form":p_form})