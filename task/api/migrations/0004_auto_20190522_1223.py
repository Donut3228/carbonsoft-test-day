# Generated by Django 2.2.1 on 2019-05-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_sensor_hardware_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorhistory',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]