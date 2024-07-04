# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'

class UserDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    gender = models.CharField(max_length=10, null=True)
    BMR = models.FloatField()
    BMI=models.FloatField()
    daily_calories = models.IntegerField(null=True)
    goal=models.CharField(max_length=10, null=True,blank=True)

    def __str__(self):
        return f'{self.username}'

class Blood(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    mobile = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.name}'

class FoodCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return f'{self.category_name}'

    @property
    def count_food_by_category(self):
        return Food.objects.filter(category=self).count()

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " (" + self.unit + ")"



class Food(models.Model):
    food_name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    description=models.TextField(null=True)
    calories = models.IntegerField(default=0)
    fat = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ManyToManyField(FoodCategory,blank=True)
    allergies = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(upload_to='foods/')
    is_featured = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient,blank=True)
    Preparation=models.TextField(null=True,blank=True)
    goal=models.CharField(max_length=10, null=True,blank=True)
    CHOICES = (
        ('Weight Loss', 'Weight Loss'),
        ('Weight Gain', 'Weight Gain') ,
        ('Weight Maintain', 'Weight Maintain'),
    )
    goal = models.CharField(max_length=20, choices=CHOICES)
    def __str__(self):
        return f'{self.food_name} - category: {self.category}'

class FoodLog(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.username.username} - {self.food_consumed.food_name}'


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restaurants/')
    food = models.ManyToManyField(Food, related_name='restaurants')

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title