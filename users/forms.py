from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class AdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email","name","family")


class AdminChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)