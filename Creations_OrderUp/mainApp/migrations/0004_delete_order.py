# Generated by Django 4.1.7 on 2023-05-03 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_alter_order_orderid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
