from django.db import models
from django.db.models import CASCADE


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
    description = models.TextField()
    image = models.ImageField(upload_to="images/", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="Products")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

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

