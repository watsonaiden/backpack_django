# Generated by Django 3.1.2 on 2020-10-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
