# Generated by Django 3.2.6 on 2021-08-27 02:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SendEmail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 2, 18, 3, 221963, tzinfo=utc)),
        ),
    ]
