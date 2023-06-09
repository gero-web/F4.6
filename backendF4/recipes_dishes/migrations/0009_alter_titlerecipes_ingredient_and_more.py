# Generated by Django 4.2 on 2023-04-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_dishes', '0008_remove_steprecipes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlerecipes',
            name='ingredient',
            field=models.ManyToManyField(related_name='title_recipes_ingredient', to='recipes_dishes.ingredient'),
        ),
        migrations.AlterField(
            model_name='titlerecipes',
            name='step_recipes',
            field=models.ManyToManyField(related_name='title_recipes_step', to='recipes_dishes.steprecipes'),
        ),
    ]
