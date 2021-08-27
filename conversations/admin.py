from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ("__str__", "created")  # 강의8.2 -1
    # pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):  # 강의8.2 - 4. admin에 표시.

    list_display = ("__str__", "count_messages", "count_participants")
