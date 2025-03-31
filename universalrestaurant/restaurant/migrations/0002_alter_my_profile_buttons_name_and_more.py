# Generated by Django 4.2.1 on 2025-03-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile_buttons',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='my_profile_buttons',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='URL'),
        ),
    ]
