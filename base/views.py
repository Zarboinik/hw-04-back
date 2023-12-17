from rest_framework import viewsets, status, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from . import models
from . import serializers


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = LimitOffsetPagination


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        # Обработка GET запроса
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Обработка POST запроса
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RecipesByCategory(generics.ListAPIView):
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return models.Recipe.objects.filter(category=category_id)
