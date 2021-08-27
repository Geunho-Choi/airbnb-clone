from django.urls import path
from rooms import views as room_views

app_name = "core"  # config > urls.py 에서 urlpattern의 namespace랑 이름이 같아야함.

# urlpatterns = [path("", room_views.all_rooms, name="home")]
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]  # 강의.11.7 -1.
# path는 오로지 url과 "함수"만 갖음.@@@@ HomeView는 클래스이기 때문에 바꿔줘야함 @@
# django에서 class based view는 view로 바꿔주는 메소드가 있음. -> as_view()
