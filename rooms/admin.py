from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
from django.utils.html import mark_safe

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


# 강의8.6 - 2. inline models 사용해서 admin안에 admin 넣기 @@.
# 사진을 room에서 바로 넣을수있게 설정.
# class PhotoInline(admin.TabularInline):
class PhotoInline(admin.StackedInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    # 강의8.6 - 3.
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                    # "city",
                ),
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # raw_id_fields # 강의8.6 - 1. foreign key를 더 나은방법으로 찾는 방법 @@@@@@
    raw_id_fields = ("host",)  # user들이 많은경우. 보기가 많은경우 쓰면 좋은 방법인듯.. 굿굿.

    search_fields = ("city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # 강의8.8 - django document에서 복사해서 가져와서.
    # def save_model(self, request, obj, form, change):
    #     # print(obj, change, form)
    #     # obj.user = request.user
    #     send_mail()
    #     super().save_model(request, obj, form, change)

    def count_amenities(self, obj):
        return obj.amenities.count()  # queryset

    count_amenities.short_description = "Amenity Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):  # 강의8.5 - 1.사용자에게 썸네일을 어드민 패널에서 보여주기.
        # print(dir(obj.file))
        # print(obj.file.url)->상대적인 url
        # print(obj.file.height) ->string뿐만아니라 많은것들을 줌. size, width..등등.
        # return obj.file.url  # 상대적인 주소 url 나옴.@ 신기...
        return mark_safe(
            f'<img width="50px" src="{obj.file.url}">'
        )  # 강의8.5 - 2. mark_safe를 import해와야지 실행됨**@@
        # 조낸신기하다..

    get_thumbnail.short_description = "Thumbnail"

    # pass
