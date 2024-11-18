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


class WebPages(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True, verbose_name="Nomi")
    link = models.CharField(max_length=500, null=True, blank=True, verbose_name="Link")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'WebPage'
        verbose_name_plural = 'Web sahifalar'
        db_table = 'web_page'

    def __str__(self):
        return self.title


class Stock(models.Model):
    title = models.CharField(max_length=221, null=True, blank=True, verbose_name="Nomi")
    image = models.ImageField(upload_to='stocks/', null=True, blank=True, verbose_name='Rasmi')
    stock_percent = models.IntegerField(null=True, blank=True, verbose_name="Chegirma foizi")
    price = models.IntegerField(null=True, blank=True, verbose_name="Narx")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = "Aksiyalar"
        db_table = 'stock'

    def __str__(self):
        return self.title


class PromoCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Foydalanuvchi")
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Aksiya")
    code = models.CharField(max_length=221, null=True, blank=True, verbose_name="Promo kod")
    is_active = models.BooleanField(default=True, null=True, blank=True, verbose_name="Aktivlik holati")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = 'PromoCode'
        verbose_name_plural = "Promo Kodlar"
        db_table = 'promocode'

    def __str__(self):
        return f"{self.user}"
