from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from catalog.models import Product, ContactInfo


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactInfoCreateView(CreateView):
    model = ContactInfo
    fields = ['name', 'email', 'phone']
    template_name = "contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_info.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "price", "description", "category", "image"]
    template_name = "add_product.html"