# Generated by Django 4.2.1 on 2025-03-30 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Зображення')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Ціна')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Знижка у %')),
                ('compound', models.TextField(blank=True, null=True, verbose_name='Інгрідієнти')),
                ('cooking_time', models.CharField(blank=True, max_length=50, null=True, verbose_name='Час приготування')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dishes.categories', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Страва',
                'verbose_name_plural': 'Страви',
                'db_table': 'Dishes',
            },
        ),
    ]
