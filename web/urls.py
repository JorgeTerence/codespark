from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("user/<str:username>/", views.user, name="user"),
    path("login/", views.login, name="login"),
    path("submit/", views.submit, name="submit"),
    path("post/<int:post_id>/", views.post, name="post"),
    path("vote/<int:post_id>/<int:choice>/", views.vote, name="vote"),
    path("", views.home, name="home"),
]
