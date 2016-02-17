from django.contrib import admin
from .models import Ingredient, Food, Element
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Element)