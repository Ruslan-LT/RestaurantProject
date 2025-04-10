"""
URL configuration for universalrestaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from restaurant.views import page_not_found
from restaurant import views
=======
from django.urls import path, include
from django.views.defaults import page_not_found
from restaurant.views import page_not_found
from restaurant import views
from restaurant import urls
>>>>>>> 2bcde29b6c4e3882e13e228b684f1ed14d675d38
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static

from universalrestaurant import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('main_page/', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
<<<<<<< HEAD
    path('main_page/', include('dishes.urls')),
    path('user/', include('users.urls')),
=======
    path('login/', views.login, name='login'),
    path('main_page/', include('dishes.urls'))
>>>>>>> 2bcde29b6c4e3882e13e228b684f1ed14d675d38
]

if settings.DEBUG:
    urlpatterns +=  debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = page_not_found