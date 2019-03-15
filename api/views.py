from django.shortcuts import render

import datetime as dt
# Create your views here.
def index(request):
    date = dt.date.today()   
  
    return render(request, 'photos/index.html', {"date": date,})