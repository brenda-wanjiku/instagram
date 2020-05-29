from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def welcome(request):
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