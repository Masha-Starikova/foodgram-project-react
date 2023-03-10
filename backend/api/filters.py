from django_filters.rest_framework import FilterSet, filters
from recipes.models import Recipe
from rest_framework.filters import SearchFilter


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(FilterSet):
    """
    Фильтры для сортировки рецептов по:
    тегам, нахождению в избранном и корзине.
    """
    tags = filters.CharFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')

    def filter_tags(self, queryset, name, value):
        if value:
            return queryset.filter(
                tags__slug__in=self.data.getlist('tags')).distinct()
        return queryset

    def filter_is_favorited(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(carts__user=self.request.user)
        return queryset
