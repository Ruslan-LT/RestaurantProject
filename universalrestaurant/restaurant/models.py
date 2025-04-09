from django.db import models

class My_profile_Buttons(models.Model):
    name = models.CharField(max_length=150,  verbose_name="Назва")
    slug = models.SlugField(max_length=200,  blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'my_profile_buttons'
        verbose_name = 'Кнопка профілю'
        verbose_name_plural = 'Кнопки профілю'

    def __str__(self):
        return self.name

