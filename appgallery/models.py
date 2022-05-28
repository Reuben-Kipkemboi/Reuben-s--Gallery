
from django.db import models
# application models

#location
class Location(models.Model):
    location =models.CharField(max_length=200)   


    def __str__(self):
        self.location
        
    def save_location(self):
        self.save()
        
        
#class Category 
class Category(models.Model):
    category =models.CharField(max_length=200)
    
    def __str__(self):
        self.category
        
    def save_category(self):
        self.save()
    
    

class Image(models.Model):
    image= models.ImageField(upload_to='photos/', null=True)
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
    
    
    
    

