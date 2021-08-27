from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    # 강의8.1 - 2.list_display해주기.
    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    # 강의8.1 - 3.progress_in 표시 해주기. ->models.py에서(왜냐하면 또 사용할거니까)

    list_filter = ("status",)
