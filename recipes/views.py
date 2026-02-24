from django.shortcuts import render  # Importa a função render para retornar templates HTML
from .models import Recipe  # Importa o model Recipe do mesmo app


def home(request):
    # QuerySet: busca no banco apenas receitas publicadas
    # filter() retorna um QuerySet lazy (só executa quando necessário)
    recipes = Recipe.objects.filter(is_published=True)

    # Renderiza o template HTML e retorna um HttpResponse
    return render(
        request,  # Objeto HttpRequest recebido pela view
        'recipes/pages/home.html',  # Caminho do template dentro da pasta templates
        status=200,  # Código HTTP da resposta (200 = OK)
        context={
            'recipes': recipes  # Dados enviados para o template (contexto)
        }
    )

from django.shortcuts import render
from .models import Recipe


def recipe(request, id):
    # Busca uma receita específica pelo id
    # filter() retorna um QuerySet, e first() pega o primeiro resultado ou None
    # Isso evita exceção caso não exista, mas exige tratamento no template
    recipe = Recipe.objects.filter(
        id=id,
        is_published=True  # garante que só receitas publicadas sejam exibidas
    ).first()

    # Renderiza a página de detalhe da receita
    return render(
        request,  # objeto HttpRequest
        'recipes/pages/recipe-view.html',  # template HTML
        status=200,  # código HTTP (opcional, Django já usa 200)
        context={
            'recipe': recipe  # envia a receita para o template
        }
    )
