from rest_framework import serializers
from .models import Recipe, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='id')

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'content']

    def to_representation(self, instance):
        representation = super(RecipeSerializer, self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation
