from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile
from .forms import AddImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    images = Image.objects.all()
    return render(request, 'homepage.html', {'images': images})


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        searched_term = request.GET.get('image')
        searched_images = Image.search_image(searched_term)
        message = f"{searched_images}"
        
        return render(request, 'search.html', {'message':message,'images':images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})


def profile(request):
    '''
    Displays a user's profile
    '''
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    images = Image.get_images(current_user)
    return render(request, 'profile.html', {"profile" : profile, "images":images} )

