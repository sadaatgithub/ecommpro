# Generated by Django 3.2.5 on 2021-09-06 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_customer_email_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]