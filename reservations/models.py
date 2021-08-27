from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    # 강의8.1 - 3.progress_in 표시해주기. checkout날짜보다 적은지를 체크.
    # checkin보다 크고, checkout보다 작으면 => in_progress표시.
    # from django.utils import timezone => timezone 가져오기. Django가 server time zone을 관리.
    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out
        # => True, False로 표시해줌.

    in_progress.boolean = True
    # => x로 표시해줌. (어떻게 아이콘으로 나오는거지...잘모르겠다.)

    # 강의8.1 - 4.is_finished 추가.
    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
