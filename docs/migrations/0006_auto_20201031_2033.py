# Generated by Django 3.1.2 on 2020-11-01 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_auto_20201012_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='last_access',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 20, 33, 26, 142705)),
        ),
        migrations.AddField(
            model_name='folder',
            name='last_access',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 20, 33, 26, 142705)),
        ),
    ]