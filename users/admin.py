from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + (
        "superhost",
    )  # 강의8.0 - 2.내꺼 필터 추가. admin끝. review바꿔주러 ㄱ.

    list_display = (  # 강의8.0 - 1.admin패널 다양하게 수정
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",  # active는 뭐지..?
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
