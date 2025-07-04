from django.urls import path
from store import views

urlpatterns = [

    path('', views.Store, name='store'),
    path('<slug:category_slug>/', views.Store, name='category_by_product'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_by_details'),
    
]