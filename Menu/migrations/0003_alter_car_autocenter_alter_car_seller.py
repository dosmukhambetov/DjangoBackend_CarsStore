# Generated by Django 4.1.3 on 2022-11-25 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_car_seller_alter_carcategory_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='autocenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='Menu.autocenter', verbose_name='AutoCenters'),
        ),
        migrations.AlterField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='Menu.seller', verbose_name='Sellers'),
        ),
    ]
