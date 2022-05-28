
from django.db import models
# application models

#location
class Location(models.Model):
    location =models.CharField(max_length=200)   


    def __str__(self):
        self.location
        
        
#class Category 
class Category(models.Model):
    category =models.CharField(max_length=200)
    
    

class Image(models.Model):
    image= models.ImageField(upload_to='photos/', null=True)
    name =models.CharField(max_length=100)
    description =models.TextField()
    date_of_upload = models.DateTimeField(auto_now_add=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    class Meta:
        ordering=['date_of_upload']
    
    
    
    

