from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comments,Like
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import ImageForm,ProfileForm,CommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts=Image.objects.all()
    return render(request, 'index.html',{"posts":posts})


@login_required(login_url='/accounts/login/')  
def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')  
def profile(request,id): 
    try: 
        current_user = request.user
        profile = Profile.objects.filter(user_id=id).all()
        images = Image.objects.filter(profile_id=current_user.profile.id).all()
        return render(request, 'profile.html', {"profile":profile, "images":images}) 
    except User.profile.RelatedObjectDoesNotExist:
        current_user = request.user
        if request.method=="POST":
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile =form.save(commit=False)
                profile.user = current_user
                profile.save()
                return render(request, 'profile.html', {"profile":profile, "images":images}) 
        else:
            form = ProfileForm()
        return render(request, 'create_profile.html',{"form":form})
    
def new_post(request):
    '''
    Enables user to upload image
    '''
    current_user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user.profile
            image.save()
        return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')  
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users =Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    

@login_required(login_url='/accounts/login/')  
def one_image(request, id):
    current_user = request.user
    image = Image.objects.get(pk=id)
    no_of_likes = image.like_set.all().count()
    comments = Comments.objects.filter(image_id=id).all()
    current_user = request.user
    image = Image.get_image_by_id(id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = current_user
            comment.image_id = image
            comment.save()
            comment = form.cleaned_data['comment']
    else:
        form= CommentForm()
    return render(request,'singlepost.html',{"image":image, "comments":comments, "no_of_likes":no_of_likes,"form":form})
@login_required(login_url='/accounts/login/')  

@login_required(login_url='/accounts/login/')       
def likes(request, id):
    current_user = request.user
    current_image = Image.objects.get(pk=id)
    new_like= Like.objects.create(user=current_user, image=current_image)
    
    return redirect(home)