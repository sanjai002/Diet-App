# Generated by Django 4.1 on 2023-11-24 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_remove_userdetails_bmi_food_bmi_foodlog_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='BMI',
        ),
    ]
