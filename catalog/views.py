from django.http import HttpResponse
from django.shortcuts import render, redirect

from catalog.models import Product, ContactInfo, Category


# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by("-created_at")[:5]
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(product)
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)

def contacts(request):
    contact_infos = ContactInfo.objects.all()
    context = {"contact_infos": contact_infos}
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html", context)

def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "product_info.html", context)

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category_name = request.POST.get("category")
        category_obj, _ = Category.objects.get_or_create(name=category_name)
        Product.objects.create(
            name=name,
            price=price,
            description=description,
            category=category_obj
        )

        return redirect("add_product")
    return render(request, "add_product.html",)