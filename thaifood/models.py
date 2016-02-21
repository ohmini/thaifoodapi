##-*-coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Element(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ธาตุ"
        verbose_name_plural = "ธาตุต่างๆ"
        db_table = 'element'


@python_2_unicode_compatible
class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    healing_element = models.ForeignKey(Element, null=True)
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "เชื้อโรค"
        verbose_name_plural = "กลุ่มเชื้อโรค"
        db_table = 'disease'


class Nutrient(models.Model):
    water = models.DecimalField(max_digits=14, decimal_places=4)
    protein = models.DecimalField(max_digits=14, decimal_places=4)
    fat = models.DecimalField(max_digits=14, decimal_places=4)
    carbohydrate = models.DecimalField(max_digits=14, decimal_places=4)
    dietary_fiber = models.DecimalField(max_digits=14, decimal_places=4)
    ash = models.DecimalField(max_digits=14, decimal_places=4)
    calcium = models.DecimalField(max_digits=14, decimal_places=4)
    phosphorus = models.DecimalField(max_digits=14, decimal_places=4)
    iron = models.DecimalField(max_digits=14, decimal_places=4)
    retinol = models.DecimalField(max_digits=14, decimal_places=4)
    beta_carotene = models.DecimalField(max_digits=14, decimal_places=4)
    vitamin_A = models.DecimalField(max_digits=14, decimal_places=4)
    vitaminE = models.DecimalField(max_digits=14, decimal_places=4)
    thiamin = models.DecimalField(max_digits=14, decimal_places=4)
    riboflavin = models.DecimalField(max_digits=14, decimal_places=4)
    niacin = models.DecimalField(max_digits=14, decimal_places=4)
    vitamin_C = models.DecimalField(max_digits=14, decimal_places=4)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.CharField(max_length=30, null=True, blank=True)
    code = models.IntegerField(default=0)

    def __str__(self):
        return 'id: ' + str(self._get_pk_val())

    class Meta:
        verbose_name = "สารอาหาร"
        verbose_name_plural = "กลุ่มสารอาหาร"
        db_table = 'nutrient'


@python_2_unicode_compatible
class IngredientCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "หมวดหมู่วัตถุดิบ"
        verbose_name_plural = "กลุ่มหมวดหมู่วัตถุดิบ"
        db_table = 'ingredient_type'


@python_2_unicode_compatible
class FoodCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "หมวดหมู่อาหาร"
        verbose_name_plural = "กลุ่มหมวดหมู่อาหาร"
        db_table = 'food_type'


@python_2_unicode_compatible
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    calories = models.IntegerField(default=0)
    nutrient = models.ForeignKey(Nutrient,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    element = models.ForeignKey(Element,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    category = models.ManyToManyField(IngredientCategory)
    healing = models.ManyToManyField(Disease, related_name="healing")
    affect = models.ManyToManyField(Disease, related_name="affect")
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.CharField(max_length=30, null=True, blank=True)
    code = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "วัตถุดิบ"
        verbose_name_plural = "กลุ่มวัตถุดิบ"
        db_table = 'ingredient'


@python_2_unicode_compatible
class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True, default="")
    calories = models.IntegerField(default=0)
    nutrient = models.ForeignKey(Nutrient,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    ingredients = models.ManyToManyField(Ingredient, through='Menu')
    category = models.ManyToManyField(FoodCategory)
    created_by = models.CharField(max_length=50, default="")
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.CharField(max_length=30, null=True, blank=True)
    code = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "อาหาร"
        verbose_name_plural = "กลุ่มอาหาร"
        db_table = 'food'


class Menu(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=14, decimal_places=4)
    name = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        db_table = 'menu'

