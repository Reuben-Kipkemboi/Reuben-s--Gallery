
from django.db import models
# application models

#location
class Location(models.model):
    location =models.CharField(max_length=200)   


    def __str__(self):
        self.location
        
        
#class Category 
class Category(models.model):
    category =models.CharField()
    
    

class Image(models.Model):
    image= models.ImageField(upload_to='photos/', null=True)
    name =models.CharField(max_length=100)
    description =models.TextField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    
    

