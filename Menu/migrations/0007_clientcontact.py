# Generated by Django 4.1.4 on 2022-12-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0006_alter_category_category_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='Subject')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Client Contact',
                'verbose_name_plural': 'Client Contacts',
                'db_table': 'client_contact',
            },
        ),
    ]
