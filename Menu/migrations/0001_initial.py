# Generated by Django 4.1.3 on 2022-11-25 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_center_name', models.CharField(max_length=100, verbose_name='Name')),
                ('auto_center_description', models.TextField(verbose_name='Description')),
                ('auto_center_location', models.TextField(verbose_name='Location')),
                ('auto_center_license', models.CharField(max_length=300, verbose_name='License')),
                ('auto_center_photo', models.ImageField(upload_to='autocenter', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Auto Center',
                'verbose_name_plural': 'Auto Centers',
                'db_table': 'autocenter',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100, verbose_name='Car Name')),
                ('car_description', models.TextField(verbose_name='Description')),
                ('car_photo', models.ImageField(upload_to='cars', verbose_name='Photo')),
                ('car_cost', models.IntegerField(verbose_name='Cars Cost')),
                ('car_data', models.DateTimeField(verbose_name='Cars Year')),
                ('autocenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='Menu.autocenter', verbose_name='AutoCenters')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_car', models.CharField(max_length=100, verbose_name='Category')),
                ('category_description', models.TextField(verbose_name='Description')),
                ('category_photo', models.ImageField(upload_to='category', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=100, verbose_name='Name')),
                ('seller_surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('seller_photo', models.ImageField(upload_to='seller', verbose_name='Photo')),
                ('seller_age', models.IntegerField(verbose_name='Age')),
                ('seller_description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
                'db_table': 'seller',
            },
        ),
        migrations.CreateModel(
            name='CarSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carssellers', to='Menu.car', verbose_name='Cars')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carssellers', to='Menu.seller', verbose_name='Sellers')),
            ],
            options={
                'verbose_name': 'Car and Seller',
                'verbose_name_plural': 'Cars and Sellers',
                'db_table': 'carseller',
            },
        ),
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carcategories', to='Menu.car', verbose_name='Books')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carcategories', to='Menu.category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Car and Category',
                'verbose_name_plural': 'Cars and Categories',
                'db_table': 'carcategory',
            },
        ),
    ]
