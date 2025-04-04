from dishes import views
from django.urls import path, include
urlpatterns = [
    path('<slug:category_slug>/', views.food_by_category, name='food_by_category'),
    path('<slug:category_slug>/<slug:dish_slug>/', views.dish_information, name='dish_information'),
]
