from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    # 8.0강의 - 1.리뷰 평균을 얻는 function만들기(반복되어짐).프론트엔드와 어드민에서 적용하기위해 model에서 만들기.

    # 8.0강의 - 3.model.py에서 만든 rating_average함수 이용해서 admin에 보여주기.
    # __str__은 그 위에 만들었던 함수. list_display에 사용할수있음.
    list_display = ("__str__", "rating_average")

    pass
