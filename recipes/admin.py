from django.contrib import admin
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

# Outra forma de registrar no admin
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Recipe, RecipeAdmin)
