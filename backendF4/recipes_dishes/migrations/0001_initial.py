# Generated by Django 4.2 on 2023-04-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('dimension', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TitleRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('time', models.TimeField()),
                ('ingredient', models.ManyToManyField(related_name='title_recipes', to='recipes_dishes.ingredient')),
            ],
        ),
    ]
