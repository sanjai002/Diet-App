# Generated by Django 4.1 on 2024-02-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0023_alter_food_category_alter_food_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
