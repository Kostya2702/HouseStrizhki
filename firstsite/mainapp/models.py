from django.db import models
from django.db.models.base import Model

class Services(models.Model):
    title = models.CharField('Название', max_length=50)
    service = models.TextField('Описание')

    def __str__(self):
        return self.title

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