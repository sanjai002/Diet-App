from django.contrib import admin
from .models import *

from django.contrib import admin

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')



class IngredientInline(admin.TabularInline):
    model = Food.ingredients.through  # Inline for the ManyToMany relationship
    extra = 1


class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'calories', 'fat', 'carbohydrates', 'protein', 'is_featured')
    inlines = [IngredientInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "ingredients":
            # Limit choices to ingredients not associated with any food
            kwargs["queryset"] = Ingredient.objects.filter(food=None)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

class RestaurantAdmin(admin.ModelAdmin):
    filter_horizontal = ('foods',)

admin.site.register(Restaurant)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Food, FoodAdmin)



admin.site.register(User)
admin.site.register(FoodCategory)
admin.site.register(UserDetails)
admin.site.register(Article)
