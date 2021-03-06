from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image,Profile,Comment
from .forms import AddImageForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def homepage(request):
    images = Image.objects.all()
    return render(request, 'homepage.html', {'images': images})


@login_required
def search_results(request):
    if 'user' in request.GET and request.GET['user']:
        searched_term = request.GET.get('user')
        profiles = Profile.search_user(searched_term)
        message = f"{searched_term}"
        
        return render(request, 'search.html', {'message':message,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})


@login_required
def profile(request):
    '''
    Displays a user's profile
    '''
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    images = Image.get_images(current_user)
    return render(request, 'profile.html', {"profile" : profile, "images":images} )



@login_required
def upload_image(request):
    if request.method == "POST":
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = request.user
            image.save()
        return redirect('homepage')
    else:
        form = AddImageForm()
    return render(request, 'image_upload.html', {"form": form})


@login_required
def update_profile(request):
    current_user = request.user

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_photo = form.cleaned_data['profile_photo']
            bio  = form.cleaned_data['bio']

            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.profile_photo = profile_photo
            updated_profile.bio = bio
            updated_profile.save()
        return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request, 'update_profile.html', {"form": form})



@login_required
def comment(request,id):
    '''
    Adds a comment
    '''
    image = Image.objects.get(pk=id)
    content = request.GET.get('comment')
    user = request.user
    comment = Comment(content = content, user = user, image = image)
    comment.save_comment()

    return redirect(get_images,id=id)


@login_required
def get_images(request,id):
    '''
    Gets the image details
    '''
    image = Image.objects.get(pk=id)
    comments = Comment.get_image_comment(image)
    total_likes = image.like_count()
    liked = False
    if image.likes.filter(id =request.user.id).exists():
        liked = True


    return render(request, 'image.html',{"image": image, "comments": comments, "total_likes": total_likes, "liked" : liked })
 
@login_required
def like_image(request,id):
    '''
    Add and delete likes
    '''
    image = Image.objects.get(pk=id)
    liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        liked = False
    else:
        image.likes.add(request.user)
        liked = True 
    return HttpResponseRedirect(reverse('get_images',args =[int(image.id)]))
