# Generated by Django 5.0.2 on 2024-02-14 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_club', '0004_alter_coach_salary_alter_manager_salary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name': 'coach', 'verbose_name_plural': 'coaches'},
        ),
        migrations.AlterField(
            model_name='coach',
            name='administration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_club.administration', verbose_name='Coach|administration'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=20, verbose_name='Coach|salary'),
        ),
    ]
