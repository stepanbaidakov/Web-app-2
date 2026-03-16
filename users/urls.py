from django.contrib.auth.views import LogoutView
from .views import Register, UserUpdateView, UserLoginView
from django.urls import path

app_name = "users"

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", UserLoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page='catalog:products_list'), name="logout"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
]
