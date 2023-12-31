# Generated by Django 4.2.5 on 2023-09-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_employee_category_alter_employee_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dismissal_date',
            field=models.CharField(verbose_name='Дата увольнения'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.CharField(verbose_name='Уникальное название'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(verbose_name='Статус'),
        ),
    ]
