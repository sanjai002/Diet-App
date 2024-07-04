# Generated by Django 4.1 on 2024-01-24 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0009_food_preparation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='preparation',
        ),
        migrations.AlterField(
            model_name='food',
            name='allergies',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='diet.foodcategory'),
        ),
    ]
