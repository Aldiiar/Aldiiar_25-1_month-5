from rest_framework import serializers
from product.models import Category, Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product_count = ProductSerializer
    class Meta:
        model = Category
        fields = 'name product_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewsStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsStarsSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title reviews rating'.split()