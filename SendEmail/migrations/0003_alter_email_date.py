# Generated by Django 3.2.6 on 2021-08-27 07:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SendEmail', '0002_alter_email_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 7, 29, 20, 191725, tzinfo=utc)),
        ),
    ]