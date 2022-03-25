from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {"password": PasswordInput()}
        labels = {
            "username": "Usuário",
            "email": "Email",
            "password": "Senha",
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {"password": PasswordInput()}
        labels = {"username": "Usuário", "password": "Senha"}


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title", "subject", "content")
        labels = {
            "title": "Título",
            "subject": "Tópico",
            "content": "Conteúdo",
        }
