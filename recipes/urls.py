from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #namespace: é para diferenciar as urls de cada app, caso haja mais de um app com a mesma url, ex: home
    path('recipes/', views.home), #namespace: é para diferenciar as urls de cada app, caso haja mais de um app com a mesma url, ex: home
    # path('contato/', views.contato),
    path('recipes/<int:id>/', views.recipe, name='recipe-view'), #namespace: é para diferenciar as urls de cada app, caso haja mais de um app com a mesma url, ex: recipe-view
]
