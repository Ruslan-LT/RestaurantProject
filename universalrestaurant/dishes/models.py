
from django.db import models
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name



class Dishes(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Зображення')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Знижка у %')
    compound = models.TextField(blank=True, null=True, verbose_name='Інгрідієнти')
    cooking_time = models.CharField(max_length=50, unique=False, null=True, blank=True, verbose_name='Час приготування')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категорія')


    class Meta:
        db_table = 'Dishes'
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * (self.discount/100), 2)



    def __str__(self):
        return self.name
