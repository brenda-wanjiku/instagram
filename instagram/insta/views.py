from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile
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