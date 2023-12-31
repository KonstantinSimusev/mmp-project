# Generated by Django 4.2.5 on 2023-09-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(verbose_name='Фамилия')),
                ('name', models.CharField(verbose_name='Имя')),
                ('patronymic', models.CharField(verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('profession', models.CharField(verbose_name='Профессия')),
                ('number', models.IntegerField(verbose_name='Личный №')),
                ('category', models.IntegerField(verbose_name='Разряд')),
                ('position', models.IntegerField(verbose_name='Штатная позиция')),
                ('schedule', models.CharField(verbose_name='График работы')),
                ('team', models.IntegerField(verbose_name='Бригада №')),
                ('employment_date', models.DateField(verbose_name='Дата трудоустройства')),
                ('dismissal_date', models.DateField(verbose_name='Дата увольнения')),
                ('area', models.CharField(verbose_name='Участок')),
                ('status', models.CharField(verbose_name='Статус')),
                ('slug', models.CharField(verbose_name='Уникальное название')),
                ('login', models.CharField(verbose_name='Логин')),
                ('password', models.CharField(verbose_name='Пароль')),
            ],
            options={
                'verbose_name_plural': 'Персонал',
            },
        ),
    ]
