# Generated by Django 3.2.5 on 2021-09-06 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_shippingaddress_customeraddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='customeraddress',
            new_name='customer',
        ),
    ]
