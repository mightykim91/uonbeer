# Generated by Django 3.1.1 on 2020-09-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0002_beer_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='brew_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
