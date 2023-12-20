from django.db import models


class Employee(models.Model):
    numeric = models.CharField('Номер сортировки')
    slug = models.CharField('Уникальное название')
    fullname = models.CharField('ФИО')
    profession = models.CharField('Профессия')
    schedule = models.CharField('График работы')
    team = models.CharField('Бригада №')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Персонал'


class TimeSheet(models.Model):
    team = models.CharField('Бригада')
    timesheet = models.TextField('Табель')

    def __str__(self):
        return f'Бригада { self.team }'

    class Meta:
        verbose_name_plural = 'Табель'