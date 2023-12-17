from django.urls import path, include
from rest_framework import routers

from base import views

router = routers.DefaultRouter()
router.register('recipes', views.RecipesViewSet)
# router.register('recipes/by_category/<int:category_id>', views.RecipesByCategory)
router.register('categorys', views.CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls), name='api'),
    path('recipes/by_category/<int:category_id>/', views.RecipesByCategory.as_view(), name='recipes-by-category'),

]
