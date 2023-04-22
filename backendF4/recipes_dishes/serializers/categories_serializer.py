from rest_framework import serializers
from recipes_dishes.models import Categories

class CategoriesSerializers(serializers.ModelSerializer):
     
     class Meta:
        model = Categories
        fields = ('title',)