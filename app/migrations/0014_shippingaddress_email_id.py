# Generated by Django 3.2.5 on 2021-09-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_customeraddress_shippingaddress_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='email_id',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
