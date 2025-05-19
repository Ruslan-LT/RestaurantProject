from django.urls import path
from orders import views

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('show-my-orders/', views.show_orders, name='show_orders'),
]