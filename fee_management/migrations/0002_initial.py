# Generated by Django 5.0.2 on 2024-11-21 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fee_management', '0001_initial'),
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management.student'),
        ),
    ]