# Generated by Django 3.1.2 on 2020-12-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(default='Your address', max_length=150, verbose_name='Delivery address'),
            preserve_default=False,
        ),
    ]
