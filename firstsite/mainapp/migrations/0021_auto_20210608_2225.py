# Generated by Django 3.1.7 on 2021-06-08 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20210608_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='map',
            field=models.FileField(upload_to='image/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
    ]
