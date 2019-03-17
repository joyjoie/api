from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Project,Profile,Comments
from . forms import ProfileUpdateForm,CommentForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Project.display_images()
    comments=Comments.display_comments()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            image_id=int(request.POST.get('image_id'))
            image=Project.objects.get(id=image_id)
            comment=form.save(commit=False)
            comment.img=image
            comment.user=request.user
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()

    context ={"images":images, "comments":comments , "form":form}
        
    return render(request, 'photos/index.html',context )

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