from django.contrib import admin

# Register your models here.

from dishes.models import Categories, Dishes

admin.site.register(Categories)
admin.site.register(Dishes)