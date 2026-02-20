from django.shortcuts import render

# # Create your views here.
# def recipe_list(request):
#     return render(request, 'recipes/recipe_list.html', {})


def home(request):
    return render(
        request,
        'recipes/pages/home.html',
        status=200,
        context={'name': 'soeirotech'}
    )
# def recipe_detail(request, recipe_id):


# def contato(request):
#     return render(request, 'temp/temp.html')
# def contato(request):
#     return render(
#         request,
#         'recipes/contato.html',
#         status=200,
#         context={'email': 'soeirotech@gmail.com'}
#     )
