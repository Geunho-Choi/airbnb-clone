# # from datetime import datetime
# from django.shortcuts import render, redirect  # 강의11.6 -1 redirect추가.


# from typing import List

# from django.views.generic.dates import timezone_today
from . import models
from django.views.generic import ListView, DetailView, View, UpdateView  # 강의 11.7 -1

from django.http import Http404  # 강의12.3

from django.urls import reverse

from django.shortcuts import render, redirect  # 강의12.0

from django_countries import countries  # 강의 13.1

# from django.utils import timezone  # 강의 11.8

# 강의11.7 -1. core>urls에서 urlpatterns바꿔주고, ListView가져오기.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room  # 어떤 모델을 list할건가.
    paginate_by = 10
    pagniate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


# def room_detail(request, pk):  # 강의 12.0 -1
#     # print(pk)  # url에서 pk를 가져옴.
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})

#     except models.Room.DoesNotExist:
#         raise Http404
# return redirect(reverse("core:home"))  # 강의12.2  링크타고 가면 보여짐...ㄹㅇ 신기하네..
# 강의 12.2 다른 이상한 숫자 주소에 막 넣어도 home으로 돌아옴.

# print(room)

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     now = timezone.now()
#     context["now"] = now
#     return context


# from math import ceil  # 강의11.2 -1
# from django.core.paginator import (
#     Paginator,
#     EmptyPage,
# )  # 강의11.4 -1, 11.6 -2 EmptyPage 추가.


# from django.http import HttpResponse

# Create your views here.
# 강의10.1 - request, response 생성.
# def all_rooms(request):  # WSGI Request임.
#     # now = datetime.now()
#     # hungry = True

#     # # return HttpResponse(content=f"<h1>{now}<h1>")
#     # # # HttpResponse를 반환. # 이렇게 수동적으로 X.-> render을 이용하자.
#     # return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
#     # # 강의 10.2 - context로 변수를 지정할수있음.@ 재밌당..ㅎㅎ

#     # all_rooms = models.Room.objects.all()

#     # 강의11.1 - 1
#     # page = request.GET.get("page", 1)
#     # page = int(page or 1)  # 강의11.2 -2. page가 없을때도 page=1로 처리.
#     # page_size = 10
#     # limit = page_size * page
#     # offset = limit - page_size
#     # # page = request.GET.get("page", 0))  # convention page. QueryDict형태로.
#     # all_rooms = models.Room.objects.all()[offset:limit]
#     # # ->django query limit 찾아보면 limit이랑 offset있음.@@

#     # # return render(request, "rooms/home.html", context={"potato": all_rooms})

#     # page_count = ceil(models.Room.objects.count() / page_size)
#     # # page_count는 '전체 방개수/페이지사이즈' 의 반올림 => 페이지수.
#     # return render(
#     #     request,
#     #     "rooms/home.html",
#     #     {
#     #         "potato": all_rooms,
#     #         "page": page,
#     #         "page_count": page_count,
#     #         "page_range": range(1, page_count),
#     #     },
#     # )
#     ###강의11.4
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()  # room_list -> 쿼리셋.(아직 db에 입력 전.)
#     paginator = Paginator(room_list, 10, orphans=5)  # Paginator가 우릴 위해서 다 해줄거임.
#     # orphans=숫자. 숫자 이하의 orphans들을 마지막 페이지에 포함시켜줌.
#     try:
#         rooms = paginator.page(int(page))
#     except EmptyPage:  # 강의11.6 예외처리
#         # rooms = paginator.page(1)
#         return redirect("/")
#     return render(request, "rooms/home.html", {"page": rooms})


class EditRoomView(UpdateView):

    model = models.Room
    template_name = "rooms/room_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )


def search(request):  # 강의13.0
    # print(request)
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    # return render(request, "rooms/search.html", {"city": city})
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")
    print(s_amenities, s_facilities)

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
    }

    room_types = models.RoomType.objects.all()

    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        # 데이터베이스에서 오는건 choices로 보냄.
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
