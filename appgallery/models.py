
from email.policy import default
from django.db import models
from django.http import Http404
from cloudinary.models import CloudinaryField
# application models

#location
class Location(models.Model):
    location =models.CharField(max_length=200)   
        
    def save_location(self):
        self.save()
        
    @classmethod
    def update_location(cls, id,updatedlocation):
        cls.objects.filter(id=id).update(image=updatedlocation)
        
        
    @classmethod
    def delete_location(cls, id):
        cls.objects.filter(id=id).delete()
    
    
    def __str__(self):
        return self.location
        
        
#class Category 
class Category(models.Model):
    category =models.CharField(max_length=200)
    
    def __str__(self):
        return self.category 
    
    def save_category(self):
        self.save()
        
    # def delete_category(self):
    #     self.category.delete()
    
    @classmethod
    def update_category(cls, id,updatedcategory):
        cls.objects.filter(id=id).update(image=updatedcategory)
    
        
    @classmethod
    def delete_category(cls, id):
        cls.objects.filter(id=id).delete()
        
   

class Image(models.Model):
    image=CloudinaryField('image')
    # image= models.ImageField(upload_to='photos/', default ="photos/p.png")
    name =models.CharField(max_length=100)
    description =models.TextField()
    date_of_upload = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering=['date_of_upload']
        
    def save_image(self):
        self.save()
        
    #delete
    @classmethod
    def delete_image(cls, id):
        cls.objects.filter(id=id).delete()
    
    #update    
    @classmethod
    def update_image(cls, id,updatedimage):
        cls.objects.filter(id=id).update(image=updatedimage)
    
    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images
        
    @classmethod
    def search_image(cls,term_of_search):
        images = cls.objects.filter(search__icontains=term_of_search)
        return images
    
    
    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images
    
    
    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category_id__category__icontains=category)
        return images
    
    
    @classmethod
    def get_images_by_id(cls, id):
        try:
            image = cls.objects.get(id=id)
            return image
        except Image.DoesNotExist:
            # print('Image does not exist')
            raise Http404()
            
    @classmethod
    def filter_by_location(cls, location_id):
        location_filter_results = Image.objects.filter(location__id =location_id)
        return location_filter_results
    
    
    
    

