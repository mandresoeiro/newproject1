from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='Geral')
    cover = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
