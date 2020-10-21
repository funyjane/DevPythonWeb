# Generated by Django 3.1.2 on 2020-10-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('biography', models.TextField(blank=True, max_length=500, null=True, verbose_name='About author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='About this genre')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=50, verbose_name='Publisher')),
                ('history', models.TextField(blank=True, max_length=500, null=True, verbose_name='More from this publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Series title')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='About the series')),
            ],
        ),
    ]