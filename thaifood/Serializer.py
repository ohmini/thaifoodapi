from rest_framework import serializers
from .models import Food, Ingredient, FoodCategory, IngredientCategory, Nutrient, Element, Disease
from django.contrib.auth.models import User
from mixins import DynamicFieldsModelSerializer


# Serializers define the API representation.
class UserSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class FoodSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('id', 'name', 'description', 'calories', 'nutrient', 'ingredients')
        depth = 1


class IngredientSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'calories', 'nutrient', 'element')
        depth = 1


class NutrientSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = '__all__'
        depth = 1


class FoodCategorySerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'
        depth = 1


class IngredientCategorySerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory
        fields = '__all__'
        depth = 1


class ElementSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
        depth = 1


class DiseaseSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('id', 'name', 'description', 'is_congenital')
        depth = 1
