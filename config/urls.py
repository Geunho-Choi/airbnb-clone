"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 강의10.0 - 1. include추가.
from django.conf import settings  # 강의8.4 - 1. 장고가 어떤 settings파일들을 내가 얘기하는지 알게될거임.
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", include("core.urls", namespace="core")),  # 강의10.0 - 2. path추가.
    # path("users", include("users.urls", namespace="users")),
    path("rooms/", include("rooms.urls", namespace="rooms")),  # 강의12.0.
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
# url이 장고에서 어떻게 동작하냐면, 왼쪽은 url. 오른쪽은 view.


if settings.DEBUG:  # 강의8.4 -2. debug상황이 아닐때, Amazon에서 온 파일들을 제공.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 신기하네 이제 사진이 보이네..ㄷㄷ
    # static파일들이 Amazon이나 다른 저장소에 의해서 제공되어질거임.
    # static파일이나 업로드된 파일들을 서버에서 사용하지마.
    # 왜냐면, 사용자가 많아지면 코드서버에서 많은 디스크공간을 소비하게됨.
