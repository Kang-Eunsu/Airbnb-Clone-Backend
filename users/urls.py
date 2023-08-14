from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path(
        "@<str:username>", views.PublicUser.as_view()
    ),  # me라는 user명을 가진 사람과 충돌할 수 있으므로 @ 기호 추가
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
]
