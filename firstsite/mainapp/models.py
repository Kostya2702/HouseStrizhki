from django.db import models
from django.db.models.base import Model

class Services(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    price = models.TextField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Title_for_section(models.Model):
    titleAboutAndPrice = models.CharField('Заголовок', default='По порядку два заголовка', max_length=150)

    def __str__(self):
        return self.titleAboutAndPrice

    class Meta:
        verbose_name = 'Заголовки'
        verbose_name_plural = 'Заголовки'


class About(models.Model):
    noteAbout = models.TextField('Напиши о вас и вашей парикмахерской')

    def __str__(self):
        return self.noteAbout
    
    class Meta:
        verbose_name = 'О парикмахерской'
        verbose_name_plural = 'О парикмахерской'


class Atmosfere(models.Model):
    photo = models.ImageField(upload_to = 'img/')

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = 'Фоточки'
        verbose_name_plural = 'Фото'


class Address(models.Model):
    city = models.CharField('Введи адрес', max_length=100)
    number = models.CharField('Введи номер телефона', max_length=20)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Адрес и телефон'
        verbose_name_plural = 'Адреса и телефоны'


