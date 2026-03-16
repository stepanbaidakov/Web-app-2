from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from users.mixins import FormControlMixin
from django import forms


class CustomUserCreationForm(FormControlMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2", "avatar", "phone_number", "country")
        usable_password = None

class CustomLoginForm(FormControlMixin, AuthenticationForm):
    pass

class CustomUserChangeForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password", "phone_number", "avatar", "country")