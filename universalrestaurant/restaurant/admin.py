from django.contrib import admin
from restaurant.models import My_profile_Buttons
# # Register your models here.
#
@admin.register(My_profile_Buttons)
class MyProfileButtonsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
