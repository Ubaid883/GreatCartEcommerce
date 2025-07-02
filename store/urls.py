from django.urls import path
from GreatCartEcommerce import views

urlpatterns = [

    path('', views.Store, name='store')
]