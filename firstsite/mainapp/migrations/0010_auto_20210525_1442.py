# Generated by Django 3.1.7 on 2021-05-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210524_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmosfere',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Добавить фото'),
        ),
        migrations.AlterField(
            model_name='services',
            name='titlePr',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок'),
        ),
    ]
