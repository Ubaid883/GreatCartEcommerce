from django.db import models
from category.models import Categorie
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    Product_name    = models.CharField(max_length=50, unique=True)
    Slug            = models.SlugField(max_length=50, unique=True)
    Description     = models.TextField()
    Price           = models.IntegerField()
    Image           = models.ImageField(upload_to='product/images')
    Stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    Created_date    = models.DateTimeField(auto_now_add=True)
    Modified_date   = models.DateTimeField(auto_now=True) 
    
    # def get_url(self):
    #     return reverse ('category_by_product',args=[self.Slug])
    
    def product_url(self):
        return reverse ('product_by_details', args=[self.category.slug,self.Slug])
    
    def __str__(self):
        return self.Product_name