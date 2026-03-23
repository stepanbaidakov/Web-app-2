from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from blog.models import BlogArticle
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
class BlogArticleCreateView(CreateView):
    model = BlogArticle
    fields = ["title", "content", "photo"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy('blog:blogs_list')


class BlogArticleListView(ListView):
    model = BlogArticle
    template_name = "blog/blog_articles_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return BlogArticle.objects.filter(is_published=True)

class BlogArticleDetailView(DetailView):
    model = BlogArticle
    template_name = "blog/blog_article_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj


class BlogArticleUpdateView(UpdateView, UserPassesTestMixin):
    model = BlogArticle
    fields = ["title", "content", "photo"]
    template_name = "blog/blog_form.html"

    def test_func(self):
        user = self.request.user
        is_content_manager = user.has_perm('catalog.delete_product')
        return is_content_manager

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})

class BlogArticleDeleteView(DeleteView):
    model = BlogArticle
    context_object_name = "blog"
    template_name = "blog/blog_article_confirm_delete.html"
    success_url = reverse_lazy('blog:blogs_list')