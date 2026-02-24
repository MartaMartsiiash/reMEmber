"""
Custom user model for the Django project.
"""


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200)

    @property
    def avatar(self):
        """
        Return the URL of the user's avatar image.
        """
        return "/static/images/avatar.png"

    def __str__(self):
        """
        Return a human-readable string representation of the user.
        """
        return f"{self.username} - {self.email}"
