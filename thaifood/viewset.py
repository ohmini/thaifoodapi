from rest_framework import viewsets
from .serializer import *
from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Food.objects.all()
        mincal = self.request.query_params.get('mincal', None)
        maxcal = self.request.query_params.get('maxcal', None)
        if mincal is not None:
            queryset = queryset.filter(calories__gt=mincal)
        if maxcal is not None:
            queryset = queryset.filter(calories__lt=maxcal)
        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        mincal = self.request.query_params.get('mincal', None)
        maxcal = self.request.query_params.get('maxcal', None)
        element = self.request.query_params.get('element', None)
        if mincal is not None:
            queryset = queryset.filter(calories__gt=mincal)
        if maxcal is not None:
            queryset = queryset.filter(calories__lt=maxcal)
        if element is not None:
            queryset = queryset.filter(code=element.lower())
        return queryset


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class IngredientCategoryViewSet(viewsets.ModelViewSet):
    queryset = IngredientCategory.objects.all()
    serializer_class = IngredientCategorySerializer


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class NutrientViewSet(viewsets.ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer
