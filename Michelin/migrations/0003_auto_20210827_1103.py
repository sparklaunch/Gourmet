# Generated by Django 3.2.6 on 2021-08-27 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Michelin', '0002_auto_20210827_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 2, 3, 57, 225363, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 2, 3, 57, 225669, tzinfo=utc)),
        ),
    ]
