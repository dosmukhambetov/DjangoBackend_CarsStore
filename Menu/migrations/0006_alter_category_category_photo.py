# Generated by Django 4.1.3 on 2022-11-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0005_car_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_photo',
            field=models.ImageField(blank=True, upload_to='photo/category', verbose_name='Photo'),
        ),
    ]
