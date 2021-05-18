from django.db import models

class Services(models.Model):
    title = models.CharField('Название', max_length=50)
    service = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class About(models.Model):
    noteAbout = models.TextField('Напиши о вас и вашей парикмахерской')

    def __str__(self):
        return self.noteAbout
    
    class Meta:
        verbose_name = 'О парикмахерской'
        verbose_name_plural = 'О парикмахерской'
