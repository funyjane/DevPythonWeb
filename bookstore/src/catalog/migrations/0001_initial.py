# Generated by Django 3.1.2 on 2020-11-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('refference_db', '0003_auto_20201024_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.ManyToManyField(to='refference_db.Genre', verbose_name='Genres')),
            ],
        ),
    ]
