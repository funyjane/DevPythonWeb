# Generated by Django 3.1.2 on 2020-11-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20201121_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='About the book'),
        ),
    ]
