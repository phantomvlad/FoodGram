from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
