from django.shortcuts import render, redirect
from .models import Image, Location, Category

# Create your views here.
def home(request):
    categories=Category.objects.all()
    locations=Location.objects.all
    all_images=Image.get_images()
    
    return render(request, 'index.html', {"templateimages":all_images, 'categorytemplates':categories, 'locations':locations})


def search(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    if 'search' in request.GET and request.GET["search"]:
        term_of_search = request.GET.get("search")
        searched_images = Image.search_image(term_of_search)
        print("*--*--*--*--*--*--*--*--*--*--*--*--*")
        print(searched_images)
        message = f"{term_of_search}"

        return render(request, 'search.html',{"message":message,"images": searched_images, 'categories':categories, 'locations':locations})

    else:
        message = "seems you have not provided a search input"
        return render(request, 'search.html',{"message":message})
      
def get_location(request, location_id):
    location_images=Image.filter_by_location(location_id)
    return render(request, 'location.html', {'images':location_images})

