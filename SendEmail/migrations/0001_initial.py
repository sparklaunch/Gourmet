# Generated by Django 3.2.6 on 2021-08-27 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 8, 27, 2, 3, 57, 227554, tzinfo=utc))),
            ],
        ),
    ]
