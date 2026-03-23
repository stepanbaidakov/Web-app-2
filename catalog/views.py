from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View
from catalog.models import Product, ContactInfo
from catalog.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

# Create your views here.

class ContactInfoCreateView(CreateView):
    model = ContactInfo
    fields = ['name', 'email', 'phone']
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Product
    template_name = "catalog/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:products_list")

    def test_func(self):
        product = self.get_object()
        user =  self.request.user
        is_owner = product.owner == user
        is_moderator = user.has_perm('catalog.delete_product')
        return is_owner or is_moderator


class ProductUnpublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации")
        product.is_active = False
        product.save()
        return redirect("catalog:products_list")
