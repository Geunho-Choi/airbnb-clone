from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from django.urls import reverse


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    # 강의8.3 - 2. upload_to="room_photos" 부분 추가.
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    # 8.8강의 - 1. save함수.
    def save(self, *arg, **kwargs):
        # self.city = "potato"
        self.city = str.capitalize(self.city)  # 앞글자를 대문자로 바꿔주기.
        super().save(*arg, **kwargs)  # django document 나온대로 똑같이.
        # 뭔지 잘 모르겠다...ㅜㅜ 암튼.. 대문자로 바꿔준다는거..

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
        # 강의 12.1 -1 override.@@
        # 이 메소드는. 내가 원하는 model을 찾을 수 있는 url을 줄거야.
        # 프론트엔드 페이지로 옮겨짐.

    # 8.0강의 - 4. 모든 review의 평균 구해보기.***@@@
    def total_rating(self):
        all_reviews = self.reviews.all()
        # review app에 보면 user foreign key를 가지고 related_name 해줬음.
        # user가 reviews를 갖는다는얘기.. 어렵네.

        # all_ratings = []  # 빈 리스트 만들어줌. 이렇게 하지말고.. 0으로..
        all_ratings = 0  # 8.1강의 - 1. total rating 완성.  하고 reservation으로..
        for review in all_reviews:
            all_ratings += review.rating_average()
        if (
            len(all_reviews) > 0
        ):  # 8.1강의 - 2. 리뷰가 없을 경우 에러발생. 그래서 없을 경우 0값을 돌려줌.(legend댓글참고)
            return round(all_ratings / len(all_reviews), 2)
        else:
            return 0

    def first_photo(self):
        # (photo,) = self.photos.all()[:1]
        # # print(photo)
        # return photo.file.url
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None
