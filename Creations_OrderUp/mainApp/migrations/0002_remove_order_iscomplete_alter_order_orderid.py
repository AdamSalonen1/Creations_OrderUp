# Generated by Django 4.1.7 on 2023-03-07 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='isComplete',
        ),
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
