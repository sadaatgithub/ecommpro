# Generated by Django 3.2.5 on 2021-09-06 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_payment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email_id',
        ),
    ]