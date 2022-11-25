# Generated by Django 4.1.3 on 2022-11-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_alter_autocenter_auto_center_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='Menu.category', verbose_name='Categories'),
        ),
    ]
