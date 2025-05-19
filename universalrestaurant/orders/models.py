from django.db import models
from dishes.models import Dishes
from users.models import User

# Create your models here.

class QueryItemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, verbose_name='Користувач', default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення замовлення')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    requires_delivery = models.BooleanField(default=False, verbose_name="Потрібна доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адресса доставки')
    payment_on_get = models.CharField(default='Картою', verbose_name='Оплата при отриманні')
    is_paid = models.BooleanField(default=False, verbose_name='Заплачено')
    status = models.CharField(max_length=50, default='В обробці', verbose_name='Статус замовлення')

    class Meta:
        db_table = 'order'
        verbose_name = 'Замовлення'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f" Замовлення № {self.pk} | Замовник {self.user.first_name} {self.user.last_name} "

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    dish = models.ForeignKey(to=Dishes, on_delete=models.SET_DEFAULT, null=True, verbose_name='Страва', default=None)
    name = models.CharField(max_length=150, verbose_name='Назва')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажу')

    class Meta:
        db_table = 'order_item'
        verbose_name = "Проданий товар"
        verbose_name_plural = "Продані товари"

    objects = QueryItemQuerySet.as_manager()


    def product_price(self):
        return round(self.dish.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Страва {self.name} | Замовлення № {self.order.pk}"

