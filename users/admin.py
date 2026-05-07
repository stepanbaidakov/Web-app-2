from django.contrib import admin

# Register your models here.
from .models import CustomUser

@admin.register(CustomUser)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'phone_number', "country")
    list_filter = ('country',)
    search_fields = ('email', "phone_number")