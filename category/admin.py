from django.contrib import admin
from .models import Categorie

# Register your models here.
class CategoryModel(admin.ModelAdmin):
    list_display = ['category_name','slug']
    prepopulated_fields={'slug':('category_name',)}
admin.site.register(Categorie, CategoryModel)
    