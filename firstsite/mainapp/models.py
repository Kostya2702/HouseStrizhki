from django.db import models
from django.db.models.base import Model
from django.utils.html import mark_safe
from django.core.validators import FileExtensionValidator


class Services(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    price = models.TextField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Hairdressers(models.Model):
    hairdresser = models.CharField('Фамилия и имя', max_length=200)
    master = models.CharField('Уровень мастерства', max_length=40)
    aboutMaster = models.CharField('Немного о мастере', max_length=255)
    avatar = models.ImageField('Добавить фото', upload_to = 'img/')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hairdresser

    class Meta:
        verbose_name = 'Парихмахер'
        verbose_name_plural = 'Парихмахеры'


class About(models.Model):
    noteAbout = models.TextField('Напиши о вас и вашей парикмахерской')

    def __str__(self):
        return self.noteAbout
    
    class Meta:
        verbose_name = 'О парикмахерской'
        verbose_name_plural = 'О парикмахерской'


class Atmosfere(models.Model):
    photo = models.ImageField(upload_to = 'img/')
    podpis = models.CharField('Подпись к фото', max_length=250)

    def image_tag(self):
        return mark_safe('<img src="/img/%s" width="150" height="150" />' % (self.photo))

    image_tag.short_description = 'Image'

    list_display = ['image_tag',]

    def __str__(self):
        return self.podpis

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


class Maps(models.Model):
    map = models.ImageField(upload_to = 'img/')

    class Meta:
        verbose_name = 'Как добраться'
        verbose_name_plural = 'Как добраться'



