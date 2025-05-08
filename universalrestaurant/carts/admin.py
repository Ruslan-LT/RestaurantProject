from django.contrib import admin
from carts.models import Cart

# Register your models here.

# admin.site.register(Cart)


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ("dish", "quantity", "created_timeswamp",)
    search_fields = ("dish", "quantity", "created_timeswamp",)
    readonly_fields = ("created_timeswamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "dish", "quantity", "created_timeswamp",)
    list_filter = ("user", "dish","created_timeswamp",)

    def user_diplay(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонімний користувач"

