from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ContactInfoCreateView

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactInfoCreateView.as_view(), name="contacts"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
    path("add_product/", ProductCreateView.as_view(), name="add_product"),
]