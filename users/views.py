from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.core.exceptions import ValidationError  


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
        return reverse_lazy("home")  # Redirect to the homepage after login
