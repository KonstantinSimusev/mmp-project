# Generated by Django 4.2.5 on 2023-10-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_alter_area_plan_alter_area_residue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='plan',
            field=models.IntegerField(verbose_name='Планируемое производство'),
        ),
        migrations.AlterField(
            model_name='area',
            name='residue',
            field=models.IntegerField(verbose_name='Остаток по смене'),
        ),
    ]
