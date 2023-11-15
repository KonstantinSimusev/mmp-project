from django.db import models


class Report(models.Model):
    date = models.CharField('Дата')
    shift = models.CharField('Смена')
    team = models.CharField('Бригада')
    report = models.TextField('Рапорт')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name_plural = 'Рапорт'


class Area(models.Model):
    slug = models.CharField('Уникальное название')
    title = models.CharField('Название участка')
    unit = models.CharField('Единица измерения показателя')
    residue = models.CharField('Остаток')
    plan = models.CharField('План')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Участки'


class Profession(models.Model):
    slug = models.CharField('Уникальное название')
    name = models.CharField('Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Профессии'
