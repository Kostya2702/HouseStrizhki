from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField

class Services(models.Model):
    titlePr = models.CharField('Заголовок', max_length=150)
    name = models.CharField('Название услуги', max_length=100)
    price = models.TextField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class About(models.Model):
    titleAbout = models.CharField('Заголовок', max_length=50)
    noteAbout = models.TextField('Напиши о вас и вашей парикмахерской')

    def __str__(self):
        return self.titleAbout
    
    class Meta:
        verbose_name = 'О парикмахерской'
        verbose_name_plural = 'О парикмахерской'


class Atmosfere(models.Model):
    photo = models.ImageField('Добвить фото')
    podpis = models.CharField('Придумай подпись к фото', max_length=90)

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = 'Атмосфера'
        verbose_name_plural = 'Атмосфера'


class Address(models.Model):
    city = models.CharField('Введи адрес', max_length=100)
    number = models.CharField('Введи номер телефона', max_length=20)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Адрес и телефон'
        verbose_name_plural = 'Адреса и телефоны'


