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
    list_display = ('name', 'category','price','discount')
    list_editable = ('price','discount',)
    search_fields = ('name','description')
    list_filter = ('category','discount')
    fields = (('name','category',),
              'slug',
              'id',
              'description',
              ('price', 'discount',),
              'compound',
              'cooking_time')