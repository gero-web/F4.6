from django.urls import path
from rest_framework.routers import DefaultRouter

from recipes_dishes.views import RecipeView,CategoriView

app_name  = 'recipe'

recipe_list = RecipeView.as_view({'get': 'list'})
recipe_retrieve = RecipeView.as_view({'get': 'retrieve'})


urlpatterns  = [
    path('recipe-categori' , CategoriView.as_view(), name='r'),
    path('recipe-categori-list/<str:categori>' , recipe_list, name='r'),
    path('recipe-categori-detail/<int:pk>' , recipe_retrieve, name='r'),
    
]