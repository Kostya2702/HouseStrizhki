# Generated by Django 3.1.7 on 2021-06-08 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20210608_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='map',
            field=models.FileField(upload_to='img/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
    ]
