from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Project,Profile,Comments
from . forms import ProfileUpdateForm,CommentForm,ProjectForm
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

def image(request, id,slug):
    image=get_object_or_404()
    try: 
        foto = Image.objects.get(id = image_id, slug=slug)

    except DoesNotExist:
        raise Http404()

    # is_liked = False
    # if image.likes.filter(id = request.user.id).exists():
    #     is_liked = True

    return render(request,"photos/image.html", {"foto":foto,"image":image})
@login_required
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

    return render(request, 'profile/profile.html', {"fo":fo,"profile":profile,"p_form":p_form,"profile":profile, "current_profile":current_profile})


def upload(request):
    if request.method =='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=ProjectForm()
    return render(request, 'photos/addimg.html', {"form":form})