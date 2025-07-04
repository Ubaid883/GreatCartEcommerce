from django.urls import path
from cart import views

urlpatterns = [

    path('', views.Cart, name='store'),

    
]