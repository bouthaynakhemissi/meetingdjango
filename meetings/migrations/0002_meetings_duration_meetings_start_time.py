# Generated by Django 5.1.1 on 2024-10-04 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='meetings',
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
