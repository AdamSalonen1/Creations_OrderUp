# Generated by Django 4.1.7 on 2023-03-07 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_remove_order_iscomplete_alter_order_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
