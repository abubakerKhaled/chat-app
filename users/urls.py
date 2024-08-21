from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordChangeDoneView,
)

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("", views.HomeView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("home/", views.HomeView.as_view(), name="home"),
    path(
        "reset-password/",
        PasswordResetView.as_view(
            template_name="auth-recoverpw.html",
            email_template_name="password_reset_email.html",
            success_url=reverse_lazy("password_reset_done"),
        ),
        name="reset_password",
    ),
    # URL for changing the password
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="change_password.html",
            success_url=reverse_lazy("password_change_done"),
        ),
        name="change_password",
    ),
    # URL for displaying the success message after password change
    path(
        "password-change-done/",
        PasswordChangeDoneView.as_view(template_name="password_change_done.html"),
        name="password_change_done",
    ),
]
