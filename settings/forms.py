# forms.py in the settings app
from django import forms
from django.contrib.auth import get_user_model


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=254)


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "profile_image",
            "status",
        ]
