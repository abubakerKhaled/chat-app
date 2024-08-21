from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from .forms import PasswordResetRequestForm
from django.views import View
from django.conf import settings


class PasswordResetView(View):
    def get(self, request):
        form = PasswordResetRequestForm()
        return render(request, "auth-recoverpw.html", {"form": form})

    def post(self, request):
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            if users.exists():
                for user in users:
                    subject = "Password Reset Requested"
                    email_template_name = (
                        "password_reset_email.html"  # Use a proper email template
                    )
                    context = {
                        "email": user.email,
                        "domain": request.META["HTTP_HOST"],
                        "site_name": "Your site name",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email_content = render_to_string(email_template_name, context)
                    send_mail(
                        subject,
                        email_content,
                        settings.EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=False,
                    )
            return redirect("password_reset_done")
        return render(request, "auth-recoverpw.html", {"form": form})
