# Generated by Django 3.1.7 on 2021-06-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_maps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='map',
            field=models.FileField(upload_to='img/'),
        ),
    ]
