from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import check_rel_lookup_compatibility
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):  # 8.0강의 - 2.리뷰 평균을 얻는 function만들기
        avg = (  # 이렇게 나만의 커스텀 함수를 모델에다가 생성할 수 있음.
            # 가끔 어드민만을 위한 함수들을 가질거임.
            # 근데 만약 그 기능을 모든 곳에 포함하고 싶다면 모델에다 넣을수있음.
            # 그건 어드민 or 프론트엔드 or 콘솔 일수도 있으니까.
            self.accuracy
            + self.communication  # self를 인자로 가져와서. 이렇게 쓰네... 신기
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)  # round로 반올림, avg뒤에 두번째로 나오는 숫자는 만들어줄 자리수.

    rating_average.short_description = "Avg."  # 위에 표시를 AVG.로 바꿔줌.
