from django.contrib import admin
from orders.models import OrderItem, Order

# admin.site.register(OrderItem)
# admin.site.register(Order)
# Register your models here.

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ('dish', 'name', 'price', 'quantity')
    search_fields = ('dish', 'name')
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'name','price', 'quantity')
    search_fields = ('order', 'product', 'name')

class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )
    readonly_fields = ('created_timestamp',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_timestamp')
    search_fields = ('id', 'is_paid', 'created_timestamp')
    list_filter = ('requires_delivery', 'payment_on_get', 'is_paid', 'status')
    readonly_fields = ('created_timestamp',)
    inlines = (OrderItemTabulareAdmin,)

