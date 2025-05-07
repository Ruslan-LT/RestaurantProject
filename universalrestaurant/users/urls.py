from users import views
from django.urls import  path

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('users-cart/', views.users_cart, name='users_cart'),
]