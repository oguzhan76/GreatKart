# Generated by Django 4.0.3 on 2022-04-09 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 13, 40, 45, 947997, tzinfo=utc)),
        ),
    ]
