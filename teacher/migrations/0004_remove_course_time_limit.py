# Generated by Django 3.0.5 on 2022-12-13 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='time_limit',
        ),
    ]
