from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile
from .forms import AddImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def homepage(request):
    images = Image.objects.all()
    return render(request, 'homepage.html', {'images': images})


@login_required
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        searched_term = request.GET.get('image')
        searched_images = Image.search_image(searched_term)
        message = f"{searched_images}"
        
        return render(request, 'search.html', {'message':message,'images':images})

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
    images = Image.get_profile_images(current_user)
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