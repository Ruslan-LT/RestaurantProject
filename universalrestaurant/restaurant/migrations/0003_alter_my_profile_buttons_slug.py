# Generated by Django 4.2.1 on 2025-03-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_my_profile_buttons_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile_buttons',
            name='slug',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
