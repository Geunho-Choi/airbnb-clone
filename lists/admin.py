from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    # 강의8.2 - 2. admin에 표시해주기.
    list_display = ("name", "user", "count_rooms")

    search_fields = ("name",)

    filter_horizontal = ("rooms",)  # 추가해줌.. 왜 추가해준건지는 모르겠음.
