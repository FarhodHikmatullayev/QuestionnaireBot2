import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ('user', 'Oddiy foydalanuvchi'),
        ('admin', 'Admin')
    )
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='F.I.Sh')
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='Username')
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='user', null=True, blank=True,
                            verbose_name='Foydalanuvchi roli')
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="Telegram ID")
    joined_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'
        db_table = 'users'

    def __str__(self):
        return self.full_name


class Channels(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True, verbose_name="Nomi")
    chat_id = models.CharField(max_length=221, null=True, blank=True, verbose_name="Chat ID")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Kanallar'
        db_table = 'channel'

    def __str__(self):
        return self.title


class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Foydalanuvchi")
    kindergarten = models.CharField(max_length=221, null=True, blank=True, verbose_name="Bog'cha")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        db_table = 'questionnaire'
        verbose_name = "Questionnaire"
        verbose_name_plural = "Atvetlar"

    def __str__(self):
        return f"{self.user.full_name}"


class Stock(models.Model):
    from_chat_id = models.BigIntegerField(null=True, blank=True, verbose_name='from chat id')
    message_id = models.BigIntegerField(null=True, blank=True, verbose_name='message id')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = "Aksiyalar"
        db_table = 'stock'

    def __str__(self):
        return f"{self.created_at}"
