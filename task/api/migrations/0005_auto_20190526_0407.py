# Generated by Django 2.2.1 on 2019-05-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190522_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorhistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
