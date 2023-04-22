from rest_framework import serializers
from recipes_dishes.models import TitleRecipes,Ingredient,StepRecipes


class IngredientSerializers(serializers.ModelSerializer):  
     class Meta:
        model = Ingredient
        fields = '__all__'
        
class StepRecipesSerializers(serializers.ModelSerializer):
   
     class Meta:
        model = StepRecipes
        fields = '__all__'
        def get_image_url(self, obj):
            return obj.image.url

class TitleRecipeDetailSerializers(serializers.ModelSerializer):
     ingredient = IngredientSerializers(read_only=True, many=True)
     step_recipes = StepRecipesSerializers(read_only=True, many=True)
     
     class Meta:
        model = TitleRecipes
        fields = '__all__'
        
class TitleRecipeListSerializers(serializers.ModelSerializer):
   
     image = serializers.SerializerMethodField(method_name='get_image_url')
     
     class Meta:
        model = TitleRecipes
        
        fields = ('id', 'title', 'time', 'image')
        
     def get_image_url(self, obj):
        request = self.context.get("request")   
        return  request.build_absolute_uri(obj.image.url) 