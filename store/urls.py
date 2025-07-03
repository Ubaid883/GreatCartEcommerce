from django.urls import path
from store import views

urlpatterns = [

    path('', views.Store, name='store'),
    path('<slug:category_slug>/', views.Store, name='category_slug'),
]