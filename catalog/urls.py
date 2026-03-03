from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("product_info/<int:product_id>/", views.product_info, name="product_info"),
    path("add_product/", views.add_product, name="add_product"),
]