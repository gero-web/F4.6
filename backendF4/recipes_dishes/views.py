from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from recipes_dishes.serializers.title_recipe_serializer import TitleRecipeDetailSerializers,\
    TitleRecipeListSerializers
from recipes_dishes.serializers.categories_serializer import CategoriesSerializers
from recipes_dishes.models import TitleRecipes,Categories


class CategoriView(viewsets.generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers


# Create your views here.
class RecipeView(viewsets.ReadOnlyModelViewSet):
    queryset = TitleRecipes.objects.all()
    serializer_class = TitleRecipeDetailSerializers
   
    def list(self, request, categori=None):
        print(categori)
        
        queryset = self.filter_queryset(self.get_queryset().filter(categories__title=categori))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TitleRecipeListSerializers(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = TitleRecipeListSerializers(queryset, many=True, context={'request': request})
        return Response(serializer.data)