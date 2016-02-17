from django.contrib import admin
from .models import Ingredient, Food, Element, FoodCategory, IngredientCategory, Nutrient, Disease
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Element)
admin.site.register(FoodCategory)
admin.site.register(IngredientCategory)
admin.site.register(Nutrient)
admin.site.register(Disease)