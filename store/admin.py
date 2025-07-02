from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug':('Product_name',)}
    list_display        = ['Product_name','Price','Stock','Category','is_available','Created_date']

admin.site.register(Product, ProductAdmin)
