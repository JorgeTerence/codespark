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
        CS = "CS", _("Ciência da Computação")
        WB = "Web", _("Desenvolvimento Web")
        DS = "Design", _("Design, UI e UX")
        MC = "Mechanics", _("Mecânica e Elétrica")
        EM = "Embeded", _("Sistemas Embarcados e Eletrônica")

    @classmethod
    def get_subjects(cls):
        return [choice[1] for choice in cls.Subject.choices]

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
