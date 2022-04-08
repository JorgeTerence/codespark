from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.test import ignore_warnings

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
        return render(request, "web/login.html", { 'form': LoginForm() })


def user(request: HttpRequest, username: str):
    user = get_object_or_404(User, username=username)
    return render(request, "web/user.html", {"user": user})


# TODO: Feed of most recent posts
def home(request: HttpRequest):
    return render(request, "web/index.html", {})


# TODO: Add a way for editing posts or at least append a note
@login_required(redirect_field_name="login")
def submit(request: HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post(
                author=request.user,
                title=form.cleaned_data["title"],
                subject=form.cleaned_data["subject"],
                content=form.cleaned_data["content"],
            )

            post.save()

            return redirect("post", post.id)

        else:
            messages.error(request, form.errors.as_text())
            return render(request, "web/submit.html", {"form": form})

    else:
        # md, code, images, videos, audio
        context = {"form": PostForm(), "subjects": Post.get_subjects()}
        return render(request, "web/submit.html", context)


def post(request: HttpRequest, post_id: int):
    pass
