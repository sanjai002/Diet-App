# Generated by Django 4.1 on 2024-01-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0008_remove_food_preparation_remove_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='preparation',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
