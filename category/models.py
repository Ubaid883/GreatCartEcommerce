from django.db import models

# Create your models here.
class Categorie(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    file = models.ImageField(upload_to='images', blank=True)