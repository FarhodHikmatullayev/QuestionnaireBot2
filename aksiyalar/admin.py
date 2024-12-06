from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'username', 'role', 'joined_at')
    list_filter = ('joined_at', 'role')
    search_fields = ('full_name', 'username')
    date_hierarchy = 'joined_at'


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'chat_id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'kindergarten', "created_at")
    list_filter = ("created_at", 'kindergarten')
    search_fields = ('user__full_name', 'kindergarten')
    date_hierarchy = 'created_at'

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_chat_id', 'message_id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('from_chat_id', 'message_id')
    date_hierarchy = 'created_at'
