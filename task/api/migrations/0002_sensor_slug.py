# Generated by Django 2.2.1 on 2019-05-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
