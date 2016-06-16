from rest_framework import viewsets
from .serializer import *
from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination
from models import Usage


def save_request(request):
    usage = Usage()
    usage.ip = request.META.get('REMOTE_ADDR')
    usage.method = request.method
    usage.path = request.path
    usage.params = request.META.get('QUERY_STRING')
    usage.save()


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
        queryset = get_query_by_nutrients(queryset, self.request)
        affects = get_query_params('affects', self.request)
        affects_all_match = get_query_params('affects_all_match', self.request)
        elements = get_query_params('elements', self.request)
        elements_all_match = get_query_params('elements_all_match', self.request)
        ingredient_params = get_query_params('ingredients', self.request)
        ingredients_all_match = get_query_params('ingredients_all_match', self.request)
        random_params = self.request.query_params.get('random', None)
        exclude_params = self.request.query_params.get('exclude', None)

        if ingredients_all_match is not None:
            ingredient_list = ingredients_all_match.split(',')
            for ingredient in ingredient_list:
                queryset = queryset.filter(ingredients__pk=ingredient)

        if affects_all_match is not None:
            affect_list = affects_all_match.split(',')
            for affect in affect_list:
                queryset = queryset.filter(ingredients__affect__pk=affect)

        if elements_all_match is not None:
            element_list = elements_all_match.split(',')
            for element in element_list:
                queryset = queryset.filter(ingredients__element__code=element)

        if ingredient_params is not None:
            ingredients = ingredient_params.split(',')
            queryset = queryset.filter(ingredients__pk__in=ingredients)

        if elements is not None:
            element_list = elements.split(',')
            queryset = queryset.filter(ingredients__element__code__in=element_list)

        if affects is not None:
            affect_list = affects.split(',')
            queryset = queryset.filter(ingredients__affect__pk__in=affect_list)

        if exclude_params is not None:
            if exclude_params == 'true':
                queryset = Food.objects.exclude(id__in=queryset)

        if random_params is not None:
            queryset = queryset.order_by('?')

        return queryset.distinct()


def get_query_by_nutrients(queryset, request):
    min_cal = get_query_params('mincalories', request)
    max_cal = get_query_params('maxcalories', request)
    min_water = get_query_params('minwater', request)
    max_water = get_query_params('maxwater', request)
    min_protien = get_query_params('minprotien', request)
    max_protien = get_query_params('maxprotien', request)
    min_fat = get_query_params('minfat', request)
    max_fat = get_query_params('maxfat', request)
    min_carbohydrate = get_query_params('mincarbohydrate', request)
    max_carbohydrate = get_query_params('maxcarbohydrate', request)
    min_diearyfiber = get_query_params('mindiearyfiber', request)
    max_diearyfiber = get_query_params('maxdiearyfiber', request)
    min_ash = get_query_params('minash', request)
    max_ash = get_query_params('maxash', request)
    min_calcium = get_query_params('mincalcium', request)
    max_calcium = get_query_params('maxcalcium', request)
    min_phosphorus = get_query_params('minphosphorus', request)
    max_phosphorus = get_query_params('maxphosphorus', request)
    min_iron = get_query_params('miniron', request)
    max_iron = get_query_params('maxiron', request)
    min_retinol = get_query_params('minretinol', request)
    max_retinol = get_query_params('maxretinol', request)
    min_betacarotene = get_query_params('minbetacarotene', request)
    max_betacarotene = get_query_params('maxbetacarotene', request)
    min_vitamina = get_query_params('minvitamin_a', request)
    max_vitamina = get_query_params('maxvitamin_a', request)
    min_vitamine = get_query_params('minvitamin_e', request)
    max_vitamine = get_query_params('maxvitamin_e', request)
    min_thiamin = get_query_params('minthiamin', request)
    max_thiamin = get_query_params('maxthiamin', request)
    min_riboflavin = get_query_params('minriboflavin', request)
    max_riboflavin = get_query_params('maxriboflavin', request)
    min_niacin = get_query_params('minniacin', request)
    max_niacin = get_query_params('maxniacin', request)
    min_vitaminc = get_query_params('minvitamin_c', request)
    max_vitaminc = get_query_params('maxvitamin_c', request)

    if min_cal is not None:
        queryset = queryset.filter(calories__gt=min_cal)
    if max_cal is not None:
        queryset = queryset.filter(calories__lt=max_cal)
    if min_water is not None:
        queryset = queryset.filter(nutrient__water__gt=min_water)
    if max_water is not None:
        queryset = queryset.filter(nutrient__water__lt=max_water)
    if min_protien is not None:
        queryset = queryset.filter(nutrient__protien__gt=min_protien)
    if max_protien is not None:
        queryset = queryset.filter(nutrient__protien__lt=max_protien)
    if min_fat is not None:
        queryset = queryset.filter(nutrient__fat__gt=min_fat)
    if max_fat is not None:
        queryset = queryset.filter(nutrient__fat__lt=max_fat)
    if min_carbohydrate is not None:
        queryset = queryset.filter(nutrient__carbohydrate__gt=min_carbohydrate)
    if max_carbohydrate is not None:
        queryset = queryset.filter(nutrient__carbohydrate__lt=max_carbohydrate)
    if min_diearyfiber is not None:
        queryset = queryset.filter(nutrient__diearyfiber__gt=min_diearyfiber)
    if max_diearyfiber is not None:
        queryset = queryset.filter(nutrient__diearyfiber__lt=max_diearyfiber)
    if min_ash is not None:
        queryset = queryset.filter(nutrient__ash__gt=min_ash)
    if max_ash is not None:
        queryset = queryset.filter(nutrient__ash__lt=max_ash)
    if min_calcium is not None:
        queryset = queryset.filter(nutrient__calcium__gt=min_calcium)
    if max_calcium is not None:
        queryset = queryset.filter(nutrient__calcium__lt=max_calcium)
    if min_phosphorus is not None:
        queryset = queryset.filter(nutrient__phosphorus__gt=min_phosphorus)
    if max_phosphorus is not None:
        queryset = queryset.filter(nutrient__phosphorus__lt=max_phosphorus)
    if min_iron is not None:
        queryset = queryset.filter(nutrient__iron__gt=min_iron)
    if max_iron is not None:
        queryset = queryset.filter(nutrient__iron__lt=max_iron)
    if min_retinol is not None:
        queryset = queryset.filter(nutrient__retinol__gt=min_retinol)
    if max_retinol is not None:
        queryset = queryset.filter(nutrient__retinol__lt=max_retinol)
    if min_betacarotene is not None:
        queryset = queryset.filter(nutrient__betacarotene__gt=min_betacarotene)
    if max_betacarotene is not None:
        queryset = queryset.filter(nutrient__betacarotene__lt=max_betacarotene)
    if min_vitamina is not None:
        queryset = queryset.filter(nutrient__vitamin_a__gt=min_vitamina)
    if max_vitamina is not None:
        queryset = queryset.filter(nutrient__vitamin_a__lt=max_vitamina)
    if min_vitaminc is not None:
        queryset = queryset.filter(nutrient__vitamin_c__gt=min_vitaminc)
    if max_vitaminc is not None:
        queryset = queryset.filter(nutrient__vitamin_c__lt=max_vitaminc)
    if min_vitamine is not None:
        queryset = queryset.filter(nutrient__vitamin_e__gt=min_vitamine)
    if max_vitamine is not None:
        queryset = queryset.filter(nutrient__vitamin_e__lt=max_vitamine)
    if min_thiamin is not None:
        queryset = queryset.filter(nutrient__thiamin__gt=min_thiamin)
    if max_thiamin is not None:
        queryset = queryset.filter(nutrient__thiamin__lt=max_thiamin)
    if min_riboflavin is not None:
        queryset = queryset.filter(nutrient__riboflavin__gt=min_riboflavin)
    if max_riboflavin is not None:
        queryset = queryset.filter(nutrient__riboflavin__lt=max_riboflavin)
    if min_niacin is not None:
        queryset = queryset.filter(nutrient__niacin__gt=min_niacin)
    if max_niacin is not None:
        queryset = queryset.filter(nutrient__niacin__lt=max_niacin)

    return queryset


def get_query_params(params, request):
    return request.query_params.get(params, None)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        queryset = get_query_by_nutrients(queryset, self.request)
        element = self.request.query_params.get('element', None)
        random_params = self.request.query_params.get('random', None)
        exclude_params = self.request.query_params.get('exclude', None)

        if element is not None:
            queryset = queryset.filter(element__code=element.lower())

        if exclude_params is not None:
            if exclude_params == 'true':
                queryset = Food.objects.exclude(id__in=queryset)

        if random_params is not None:
            queryset = queryset.order_by('?')

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
