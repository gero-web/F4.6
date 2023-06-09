# Generated by Django 4.2 on 2023-04-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_dishes', '0003_alter_titlerecipes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('number', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='titlerecipes',
            name='step_recipes',
            field=models.ManyToManyField(related_name='title_recipes', to='recipes_dishes.steprecipes'),
        ),
    ]
