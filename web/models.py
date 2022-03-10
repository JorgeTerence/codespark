from django.db.models import *
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Account(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    bio = TextField(default="")
    karma = IntegerField(default=0)
    publisher = BooleanField(default=False)
    avatar = ImageField(upload_to="avatars", blank=True, null=True)
    stats = JSONField(default=dict)


class Post(Model):
    class Subject(TextChoices):
        PY = "Py", _("Python")
        JAVA = "Java", _("Java")
        CSHARP = "C#", _("C#")
        JS = "JS", _("Javascript")
        PHP = "PHP", _("PHP")
        MOBILE = "Mobile", _("Mobile")
        INO = "Ino", _("Arduino")
        DB = "DB", _("Base de Dados")
        WEB = "WEB", _("Web Dev")
        UI = "UI", _("UI / UX")
        CS = "CS", _("Ciência da Computação")
        LX = "LX", _("GNU / Linux")

    author = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=127)
    content = TextField()
    votes = IntegerField(default=0)
    subject = CharField(
        max_length=31,
        choices=Subject.choices,
        default=Subject.CS,
    )


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE)
    author = ForeignKey(User, on_delete=CASCADE)
    content = TextField()
    votes = IntegerField()