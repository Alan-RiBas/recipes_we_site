from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=168)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=16)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=16)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publushed = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
