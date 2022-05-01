import json
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import LoginForm, PostForm, RegisterForm
from .models import Account, Post


def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            Account(user=user).save()

            django_login(request, user)

            return redirect("user", user.username)

        else:
            messages.error(request, form.errors.as_text())
            return render(request, "web/register.html", {"form": form})

    else:
        return render(request, "web/register.html", {"form": RegisterForm()})


def login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                django_login(request, user)
                return redirect("user", username)

            else:
                messages.error(request, "Falha de autenticação. Tente novamente")
                return redirect("login")

        else:
            messages.error(request, "Usuário ou senha inválidos!")
            return render(request, "web/login.html", {"form": form})

    else:
        return render(request, "web/login.html", {"form": LoginForm()})


def user(request: HttpRequest, username: str):
    user = get_object_or_404(User, username=username)
    return render(request, "web/user.html", {"user": user})


def home(request: HttpRequest):
    return render(request, "web/index.html", {"posts": Post.objects.all()})


# TODO: Add a way for editing posts or append a note
# TODO: Check for possible errors
# IDEA: use a hash of the title instead of the id for the url
# FIXME: Block duplicate titles
# FIXME: MariaDB doesn't accept emojis (can't have emojis on post)
@login_required(redirect_field_name="login")
def submit(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body.decode())

        post = Post(
            author=request.user,
            title=data["title"],
            subject=data["subject"],
            content=data["content"],
            peek=data["peek"],
        )
        post.save()

        return redirect("post", post.id)

    else:
        context = {"form": PostForm(), "subjects": Post.Subject.choices}
        return render(request, "web/submit.html", context)


def post(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "web/post.html", {"post": post})


def vote(request: HttpRequest, post_id: int, choice: int):
    post = get_object_or_404(Post, id=post_id)
    if choice > 0:
        post.votes += 1
    elif choice < 0:
        post.votes -= 1
    else:
        return HttpResponse("What do you whant me to do >:(")  # Return troll page
    return HttpResponse(True)
