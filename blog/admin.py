from django.contrib import admin

# Register your models here.
from .models import BlogArticle

@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'views')
    list_filter = ('publication_date',)
    search_fields = ('title',)