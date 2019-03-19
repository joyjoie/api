from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Project,Profile,Comments,Ratings
from . forms import ProfileUpdateForm,CommentForm,ProjectForm,RatingsForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer,ProjectSerializer

class ProfileList(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.get(user=request.user)
        serializers = ProfileSerializer(profile, many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        all_stuff = Project.objects.all()
        serializers = ProjectSerializer(all_stuff, many=True)
        return Response(serializers.data)

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Project.display_images()
    comments=Comments.display_comments()
    ratings=Ratings.display_ratings()
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


   

    context ={"images":images, "comments":comments , "form":form, }
        
    return render(request, 'photos/index.html',context )

@login_required(login_url='/accounts/login/')
def project(request,id):
    project=Project.objects.get(id=id)

    
    if request.method=='POST':
        form=RatingsForm(request.POST)
        if form.is_valid():
            project_id=int(request.POST.get('project_id'))
            project=Project.objects.get(id=project_id)
            rating=form.save(commit=False)
            rating.pr=project
            rating.user=request.user
            rating.save()
            return redirect('project', project.id)
    else:
        form=RatingsForm()

    ratings= Ratings.objects.filter(pr=project)


    return render(request, 'photos/project.html', { "project":project,"form":form,"ratings":ratings}) 


@login_required(login_url='/accounts/login/')
def my_profile(request):
    profile = request.user.profile   
    # images = Project.objects.all().filter(id = profile.user.id)
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
    return render(request, 'profile/profile.html', { "profile":profile, "p_form":p_form })



@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile=Profile.objects.get(id=id)
    
    if request.method == 'POST':
       
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',profile.id)

    else:
        
        p_form = ProfileUpdateForm(instance=request.user.profile)

    fo=Profile.pro()
    profile=Profile.objects.get(id=id)
    current_profile=Profile.objects.get(user=request.user)

    return render(request, 'profile/profile.html', {"fo":fo,"p_form":p_form,"profile":profile, "current_profile":current_profile})


def upload(request):
    if request.method =='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=ProjectForm()
    return render(request, 'photos/addimg.html', {"form":form})



