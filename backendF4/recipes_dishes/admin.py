from django.contrib import admin
from recipes_dishes.models import Ingredient,TitleRecipes \
    , StepRecipes, Categories
# Register your models here.



admin.site.register(Ingredient)
admin.site.register(StepRecipes)
admin.site.register(Categories)
admin.site.register(TitleRecipes)
