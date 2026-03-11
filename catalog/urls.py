from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ContactInfoCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = "catalog"

urlpatterns = [
    path("contacts/", ContactInfoCreateView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

]