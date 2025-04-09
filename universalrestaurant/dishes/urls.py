from dishes import views
<<<<<<< HEAD
from django.urls import path

=======
from django.urls import path, include
>>>>>>> 2bcde29b6c4e3882e13e228b684f1ed14d675d38
urlpatterns = [
    path('search/', views.food_by_category, name='search'),
    path('<slug:category_slug>/', views.food_by_category, name='food_by_category'),
    path('<slug:category_slug>/<slug:dish_slug>/', views.dish_information, name='dish_information'),
]
