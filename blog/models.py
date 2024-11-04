from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = RichTextField()
    tags = models.CharField(max_length=255, blank=True, help_text="Separate tags with commas.")
    category = models.ManyToManyField(Category, related_name="posts")
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def snip(self):
        return f"{self.content[:100]}..."

    @property
    def is_published(self):
        return self.status and self.published_date is not None


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
