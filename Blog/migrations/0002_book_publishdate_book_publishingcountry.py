# Generated by Django 5.0.7 on 2024-07-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publishDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publishingCountry',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
