from django.shortcuts import render
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True)
    return render(
        request,
        'recipes/pages/home.html',
        status=200,
        context={'recipes': recipes}
    )
