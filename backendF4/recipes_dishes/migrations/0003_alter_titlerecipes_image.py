# Generated by Django 4.2 on 2023-04-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_dishes', '0002_titlerecipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlerecipes',
            name='image',
            field=models.ImageField(upload_to='upload_images'),
        ),
    ]
