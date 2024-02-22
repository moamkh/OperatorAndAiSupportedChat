from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extara_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extara_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

USER = 'user'
OPERATOR = 'operator'
ADMIN = 'admin'
STATUS_CHOICES = (
    (USER, 'user'),
    (OPERATOR, 'operator'),
    (ADMIN, 'admin'),
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    name = models.CharField(_("name"), max_length=150, blank=True)
    family = models.CharField(_("family"), max_length=150, blank=True)
    status = models.CharField(default="user", choices=STATUS_CHOICES, max_length=128)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password","name","family","status"]

    objects = UserManager()

    def __str__(self):
        return self.email
