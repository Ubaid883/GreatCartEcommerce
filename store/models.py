from django.db import models
from category.models import Categorie

# Create your models here.
class Product(models.Model):
    Product_name    = models.CharField(max_length=50, unique=True)
    Slug            = models.SlugField(max_length=50, unique=True)
    Description     = models.TextField()
    Price           = models.IntegerField()
    Image           = models.ImageField(upload_to='product/images')
    Stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    Category        = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    Created_date    = models.DateTimeField(auto_now_add=True)
    Modified_date   = models.DateTimeField(auto_now=True) 
    
    
    def __str__(self):
        return self.Product_name