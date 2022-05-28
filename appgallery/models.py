
from email.policy import default
from django.db import models
# application models

#location
class Location(models.Model):
    location =models.CharField(max_length=200)   
        
    def save_location(self):
        self.save()
        
        
#class Category 
class Category(models.Model):
    category =models.CharField(max_length=200)
    
        
    def save_category(self):
        self.save()
    
    

class Image(models.Model):
    image= models.ImageField(upload_to='photos/', default ="photos/p.png")
    name =models.CharField(max_length=100)
    description =models.TextField()
    date_of_upload = models.DateTimeField(auto_now_add=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def _str_(self):
        self.name
        
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
    def search_image(cls,term_of_search):
        images = cls.objects.filter(search__icontains=term_of_search)
        return images
    
    
    
    
    
    

