from django.urls import path
from . import views


app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.search, name="search"),
]
# urlpatterns = [path("<int:pk>/edit/", views.EditRoomView.as_view(), name="edit")]

# django path 구글 검색. 참조하기.
