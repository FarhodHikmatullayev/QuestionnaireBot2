# Generated by Django 5.1.3 on 2024-11-29 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aksiyalar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 29, 19, 3, 33, 455379), null=True, verbose_name='Yaratilgan vaqti'),
        ),
    ]
