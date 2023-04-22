from django.db import models

# Create your models here.


class Ingredient(models.Model):
    
    title = models.CharField(max_length=30, unique=True)
    dimension  = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.title
    
class Categories(models.Model):
    
    title = models.CharField(max_length=30, unique=True)
     
    def __str__(self) -> str:
        return self.title


class StepRecipes(models.Model):
    
   number = models.PositiveSmallIntegerField()
   image = models.ImageField(upload_to='upload_images/steps')
   description = models.TextField()
   
   def __str__(self) -> str:
        return self.description[:10]

class TitleRecipes(models.Model):
    
    title = models.CharField(max_length=125)
    time = models.PositiveSmallIntegerField()
    ingredient = models.ManyToManyField(to=Ingredient, related_name="title_recipes")
    step_recipes = models.ManyToManyField(to=StepRecipes, related_name="title_recipes")
    image = models.ImageField(upload_to='upload_images')
    categories = models.ForeignKey(to=Categories, related_name='title_recipes',  on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    