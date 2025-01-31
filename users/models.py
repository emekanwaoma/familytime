import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models

from resume_summarizer.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "username",
    ]

    def user_full_name(self):
        return self.get_full_name().capitalize()

    @staticmethod
    def generate_username(prefix):
        random_string = "".join(random.choices(string.ascii_lowercase, k=6))
        return f"{prefix}{random_string}"

