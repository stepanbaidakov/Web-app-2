from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm, CustomUserChangeForm, CustomLoginForm
from config.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


# Create your views here.

class Register(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        response = super().form_valid(form)  # сохраняет self.object и делает редирект
        login(self.request, self.object)  # логиним пользователя после сохранения
        self.send_welcome_email(self.object.email)
        return response

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = f'Спасибо, что зарегистрировались в нашем сервисе, {user_email}!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("catalog:products_list")

    def get_object(self, queryset=None):
        # редактируем текущего пользователя
        return self.request.user

class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "users/login.html"