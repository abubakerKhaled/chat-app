from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "date_joined",
        "is_staff",
    )  # Columns to display in the list view
    search_fields = ("username", "email")  # Add a search bar
    list_filter = ("is_staff", "is_active")  # Add filters on the right side


admin.site.register(CustomUser, CustomUserAdmin)
