from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def home(request):
    all_images = Image.objects.all()
    return render(request, 'index.html', {"templateimages":all_images})
