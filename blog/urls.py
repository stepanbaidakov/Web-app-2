from django.urls import path
from .views import BlogArticleListView, BlogArticleDetailView, BlogArticleDeleteView, BlogArticleUpdateView, \
    BlogArticleCreateView

app_name = "blog"

urlpatterns = [
    path("blog/", BlogArticleListView.as_view(), name="blogs_list"),
    path("blog/<int:pk>/", BlogArticleDetailView.as_view(), name="blog_detail"),
    path("blog/new/", BlogArticleCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/edit/", BlogArticleUpdateView.as_view(), name="blog_edit"),
    path("blog/<int:pk>/delete/", BlogArticleDeleteView.as_view(), name="blog_delete"),
]
