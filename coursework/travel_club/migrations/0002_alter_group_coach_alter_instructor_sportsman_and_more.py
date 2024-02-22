# Generated by Django 5.0.2 on 2024-02-14 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='travel_club.coach'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='sportsman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel_club.sportsman'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel_club.group'),
        ),
    ]