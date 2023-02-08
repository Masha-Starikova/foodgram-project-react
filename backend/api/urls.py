from django.urls import include, path
from rest_framework import routers

from .views import IngredientsViewSet, RecipeViewSet, TagsViewSet

v1_router = routers.DefaultRouter()
v1_router.register('recipes', RecipeViewSet, basename='recipes')
v1_router.register('ingredients', IngredientsViewSet, basename='ingredients')
v1_router.register('tags', TagsViewSet, basename='tags')

urlpatterns = [
    path('', include(v1_router.urls)),
]
