# Generated by Django 3.2.6 on 2021-08-27 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SendEmail', '0005_alter_email_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 8, 32, 25, 933927, tzinfo=utc)),
        ),
    ]
