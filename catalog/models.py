from django.db import models
from django.db.models import CASCADE
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="Products", verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    is_active = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="Products", verbose_name="Владелец", blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']
        permissions = [("can_unpublish_product", "Can unpublish product")]


class ContactInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Contacts"
        verbose_name = "Cantact information"
        verbose_name_plural = "Cantact information"

