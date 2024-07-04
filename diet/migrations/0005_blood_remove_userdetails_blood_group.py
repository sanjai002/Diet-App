# Generated by Django 4.1 on 2023-12-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0004_alter_food_allergies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='Blood_group',
        ),
    ]
