# Generated by Django 3.1.2 on 2020-12-01 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_delivery_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-create_date']},
        ),
    ]
