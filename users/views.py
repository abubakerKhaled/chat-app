from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import (
    LoginView as AuthLoginView,
    LogoutView as AuthLogoutView,
)
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "auth-register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)  # Log the user in after signup
                return redirect(
                    "home"
                )  # Redirect to the home page after successful signup
            except ValidationError as e:
                form.add_error(None, str(e))
        return render(request, "auth-register.html", {"form": form})


class LoginView(AuthLoginView):
    template_name = "auth-login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class ResetPassword(TemplateView):
    template_name = "auth-recoverpw.html"


class CustomLogoutView(View):
    def get(self, request):
        logout(request)  # Log the user out
        return redirect("login")  # Redirect to the login page


# TODO: make the update profile template and view and urls work
# @login_required
# def update_profile(request):
#     if request.method == "POST":
#         form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect("profile")  # Redirect to the profile page after updating
#     else:
#         form = UserProfileUpdateForm(instance=request.user)
#     return render(request, "users/update_profile.html", {"form": form})
