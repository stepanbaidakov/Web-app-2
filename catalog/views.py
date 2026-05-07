from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View
from catalog.models import Product, ContactInfo, Category
from catalog.forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import CategoryService
from django.core.cache import cache
# Create your views here.

class ContactInfoCreateView(CreateView):
    model = ContactInfo
    fields = ['name', 'email', 'phone']
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("products_list")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("products_list", queryset, 60 * 15)
        return queryset


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


class CategoryProductsView(DetailView):
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.object.id
        context["products"] = CategoryService.products_in_category(category_id)
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/categories_list.html"
    context_object_name = "categories"
