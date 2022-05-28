from django.shortcuts import render, redirect
from .models import Image, Location, Category

# Create your views here.
def home(request):
    # all_images = Image.objects.all()
    categories=Category.objects.all()
    locations=Location.objects.all
    all_images=Image.get_images()
    
    # if request.GET.get('location'):
    #     all_images = Image.filter_by_location(request.GET.get('location'))
    #     return render(request, 'location.html', {'images':all_images, 'categories':categories, 'location': request.GET.get('location')})
    return render(request, 'index.html', {"templateimages":all_images, 'categorytemplates':categories,'localtemplates':locations })


def search(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    if 'search' in request.GET and request.GET["search"]:
        term_of_search = request.GET.get("search")
        searched_images = Image.search_image(term_of_search)
        print("___________________________________________")
        print(searched_images)
        message = f"{term_of_search}"

        return render(request, 'search.html',{"message":message,"images": searched_images, 'categories':categories, 'locations':locations})

    else:
        message = "seems you have not provided a search input"
        return render(request, 'search.html',{"message":message})
    
        
def image_location(request):
    location_images=Location.objects.all()
    return render(request, 'location.html')