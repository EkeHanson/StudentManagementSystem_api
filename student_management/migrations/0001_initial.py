# Generated by Django 5.0.2 on 2024-11-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('class_assigned', models.CharField(max_length=50)),
                ('section', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
