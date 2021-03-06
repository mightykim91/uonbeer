# Generated by Django 3.1.1 on 2020-09-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0003_beer_brew_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='image_file_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='image_url',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
