from .models import User

from django.contrib import admin
from .forms import AdminCreationForm, AdminChangeForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAdminSite(UserAdmin):
    add_form = AdminCreationForm
    form = AdminChangeForm
    model = User
    list_display = ("pk", "email", "is_staff", "is_active", "name", "family", "status")
    list_filter = ("email", "is_staff", "is_active", "name", "family", "status")
    fieldsets = (
        (None, {"fields": ("email", "password", "status")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "name", "family", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdminSite)
