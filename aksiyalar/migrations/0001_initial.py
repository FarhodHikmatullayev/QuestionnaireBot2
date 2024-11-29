# Generated by Django 5.1.3 on 2024-11-29 03:29

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nomi')),
                ('chat_id', models.CharField(blank=True, max_length=221, null=True, verbose_name='Chat ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name="Qo'shilgan vaqti")),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Kanallar',
                'db_table': 'channel',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='F.I.Sh')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('role', models.CharField(blank=True, choices=[('user', 'Oddiy foydalanuvchi'), ('admin', 'Admin')], default='user', max_length=100, null=True, verbose_name='Foydalanuvchi roli')),
                ('telegram_id', models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Telegram ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name="Qo'shilgan vaqti")),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Foydalanuvchilar',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindergarten', models.CharField(blank=True, max_length=221, null=True, verbose_name="Bog'cha")),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2024, 11, 29, 8, 29, 27, 273586), null=True, verbose_name='Yaratilgan vaqti')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aksiyalar.user', verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Questionnaire',
                'verbose_name_plural': 'Atvetlar',
                'db_table': 'questionnaire',
            },
        ),
    ]
