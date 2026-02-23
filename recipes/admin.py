from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'is_published')
    list_filter = ('category', 'is_published', 'created_at')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
