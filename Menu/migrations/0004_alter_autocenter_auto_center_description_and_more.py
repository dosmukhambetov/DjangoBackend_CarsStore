# Generated by Django 4.1.3 on 2022-11-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_alter_car_autocenter_alter_car_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autocenter',
            name='auto_center_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='autocenter',
            name='auto_center_photo',
            field=models.ImageField(upload_to='photo/autocenter', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photo/cars', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_photo',
            field=models.ImageField(upload_to='photo/category', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_photo',
            field=models.ImageField(upload_to='photo/seller', verbose_name='Photo'),
        ),
    ]
