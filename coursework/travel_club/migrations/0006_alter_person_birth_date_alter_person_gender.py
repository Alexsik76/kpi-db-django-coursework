# Generated by Django 5.0.2 on 2024-02-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_club', '0005_alter_coach_options_alter_coach_administration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.IntegerField(choices=[(1, 'чоловік'), (2, 'жінка')], default=1, verbose_name='gender'),
        ),
    ]
