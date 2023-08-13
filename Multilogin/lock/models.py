from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pin_password = models.IntegerField(null=True)

class Session_pin(models.Model):
    session_code = models.CharField(max_length=200,
        help_text="session_code hasable"
    )
    user = models.OneToOneField(User,
        on_delete = models.SET_NULL,
        help_text="this is user",
        null= True
    )

    def __str__(self) -> str:
        return self.user.username


