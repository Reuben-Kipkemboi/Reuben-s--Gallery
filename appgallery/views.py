from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def home(request):
    all_images = Image.objects.all()
    return render(request, 'index.html', {"templateimages":all_images})


def search(request):
    if 'search' in request.GET and request.GET["search"]:
        term_of_search = request.GET.get("search")
        searched_images = Image.search_image(term_of_search)
        print(searched_images)
        message = f"{term_of_search}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "seems you have not provided a search input"
        return render(request, 'search.html',{"message":message})
