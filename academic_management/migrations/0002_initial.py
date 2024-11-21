# Generated by Django 5.0.2 on 2024-11-21 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_management', '0001_initial'),
        ('teacher_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='teacher_management.teacher'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_management.subject'),
        ),
    ]