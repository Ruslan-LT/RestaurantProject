from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from restaurant.views import page_not_found




from restaurant import views
urlpatterns = [
    path('sea_food/', views.sea_food, name='sea_food'),
    path('normal_food/', views.normal_food, name='normal_food'),
    path('meat_food/', views.meat_food, name='meat_food'),
]


