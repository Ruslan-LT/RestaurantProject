from dishes import views
from django.urls import path, include
urlpatterns = [
    path('sea_food/', views.sea_food, name='sea_food'),
    path('normal_food/', views.normal_food, name='normal_food'),
    path('meat_food/', views.meat_food, name='meat_food'),
    path('sea_food/<slug:dish_slug>/', views.dish_information, name='information'),
    path('normal_food/<slug:dish_slug>/', views.dish_information, name='information'),
    path('meat_food/<slug:dish_slug>/', views.dish_information, name='information'),
]
