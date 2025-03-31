from django.contrib import admin

# Register your models here.

from dishes.models import Categories, Dishes


# admin.site.register(Categories)
# admin.site.register(Dishes)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}