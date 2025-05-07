from django.db import models
from users.models import User
from dishes.models import Dishes

# Create your models here.


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):

    user = models.ForeignKey(to=User,blank=True,null=True, on_delete=models.CASCADE, verbose_name='Користувач')
    dish = models.ForeignKey(to=Dishes, on_delete=models.CASCADE, verbose_name='Страва')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, null=True, blank=True,)
    created_timeswamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    class Meta:
        db_table = 'cart'
        verbose_name = "Кошик"
        verbose_name_plural = verbose_name

    def product_price(self):
        return round(self.dish.sell_price() * self.quantity, 2)

    objects = CartQueryset().as_manager()


    def __str__(self):
        return f"Корзина {self.user.username } | Страва {self.dish.name} | Кількість {self.quantity}"
