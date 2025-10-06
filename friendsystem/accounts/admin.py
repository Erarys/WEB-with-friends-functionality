from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import EmailUserCreationForm, UserUpdateForm


@admin.register(User)
class EmailUserAdmin(UserAdmin):
    add_form = EmailUserCreationForm
    form = UserUpdateForm
    model = User

    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Персональные данные", {"fields": ("first_name", "last_name", "avatar", "bio", "date_of_birth")}),
        ("Права доступа", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
