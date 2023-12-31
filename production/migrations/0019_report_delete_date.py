# Generated by Django 4.2.5 on 2023-10-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0018_date_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(verbose_name='Дата')),
                ('shift', models.CharField(verbose_name='Смена')),
                ('team', models.CharField(verbose_name='Бригада')),
                ('report', models.TextField(verbose_name='Рапорт')),
            ],
            options={
                'verbose_name_plural': 'Рапорт',
            },
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
