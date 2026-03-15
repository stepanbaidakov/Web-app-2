from django.db import models

# Create your models here.
class BlogArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    photo = models.ImageField(upload_to='images', verbose_name="Photo")
    publication_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Is published")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Article"
        verbose_name_plural = "Blog Articles"