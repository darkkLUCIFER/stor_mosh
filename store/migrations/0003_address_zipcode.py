# Generated by Django 3.2.4 on 2022-12-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=255, null=True),
        ),
    ]