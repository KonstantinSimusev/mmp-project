from django.db import models


class Employee(models.Model):
    slug = models.CharField('Уникальное название')
    fullname = models.CharField('ФИО')
    # name = models.CharField('Имя')
    # patronymic = models.CharField('Отчество')
    # birthday = models.CharField('Дата рождения')
    profession = models.CharField('Профессия')
    # probation = models.CharField('Стажировка')
    # number = models.CharField('Личный №')
    # category = models.CharField('Разряд')
    # position = models.CharField('Штатная позиция')
    schedule = models.CharField('График работы')
    team = models.CharField('Бригада №')
    # employment_date = models.CharField('Дата трудоустройства')
    # dismissal_date = models.CharField('Дата увольнения')
    # area = models.CharField('Участок')
    # presence = models.CharField('Присутствие на рабочем месте')
    # numeric = models.CharField('Номер сортировки')
    # status = models.CharField('Статус')
    # login = models.CharField('Логин')
    # password = models.CharField('Пароль')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Персонал'


class TimeSheet(models.Model):
    team = models.CharField('Бригада')
    timesheet = models.TextField('Табель')

    def __str__(self):
        return f'Бригада {self.team}'

    class Meta:
        verbose_name_plural = 'Табель'