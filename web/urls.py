from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("user/<str:username>/", views.user, name="user"),
    path("login/", views.login, name="login"),
    path("submit/", views.submit, name="submit"),
    path("", views.home, name="home"),
]
