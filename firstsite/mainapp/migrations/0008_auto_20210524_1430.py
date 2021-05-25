# Generated by Django 3.1.7 on 2021-05-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210521_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='service',
        ),
        migrations.AddField(
            model_name='services',
            name='name',
            field=models.CharField(default=123, max_length=100, verbose_name='Название услуги'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='price',
            field=models.TextField(default=333, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
    ]
