from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, ContactInfo


# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by("-created_at")[:5]
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(product)
    return render(request, "home.html", )

def contacts(request):
    contact_infos = ContactInfo.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html", {"contact_infos": contact_infos})