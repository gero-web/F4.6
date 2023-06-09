# Generated by Django 4.2 on 2023-04-21 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_dishes', '0009_alter_titlerecipes_ingredient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='titlerecipes',
            name='ingredient',
            field=models.ManyToManyField(related_name='title_recipes', to='recipes_dishes.ingredient'),
        ),
        migrations.AlterField(
            model_name='titlerecipes',
            name='step_recipes',
            field=models.ManyToManyField(related_name='title_recipes', to='recipes_dishes.steprecipes'),
        ),
        migrations.AddField(
            model_name='titlerecipes',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='title_recipes', to='recipes_dishes.categories'),
        ),
    ]
