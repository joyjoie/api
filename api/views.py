from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Project
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Project.display_images()
    date = dt.date.today()   
  
    return render(request, 'photos/index.html', {"images":images,"date": date,})