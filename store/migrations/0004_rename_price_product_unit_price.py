# Generated by Django 3.2.4 on 2022-12-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_zipcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
