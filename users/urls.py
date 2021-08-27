from django.urls import path
from . import views

app_name = "users"

# 강의 14.0 - 1. urlpatterns 만들고 시작.
urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
]
