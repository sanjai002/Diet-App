# Generated by Django 4.1 on 2024-03-01 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0028_goal_alter_food_preparation_alter_ingredient_unit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='Goal',
            new_name='goal',
        ),
    ]
