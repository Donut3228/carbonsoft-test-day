# Generated by Django 2.2.1 on 2019-05-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_sensor_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='hardware_name',
        ),
    ]
