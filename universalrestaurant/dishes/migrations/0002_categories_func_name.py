# Generated by Django 5.1.7 on 2025-04-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='func_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Назва URL маршрута, який відпрацьовує'),
        ),
    ]
