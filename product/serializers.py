from rest_framework import serializers
from product.models import Category, Product, Review
from rest_framework.exceptions import ValidationError


class ReviewsStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsStarsSerializer(many=True)
    class Meta:
        model = Product
        fields = 'title reviews rating'.split()


class ProductValidateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(required=False, default="No description")
    price = serializers.FloatField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found!')
        return category_id

    class Meta:
        model = Product
        fields = 'id title description price category_id'.split()


class CategoryValidateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150, min_length=3)
    product_count = ProductValidateSerializer

    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ReviewValidateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=500)
    stars = serializers.IntegerField(required=False, min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product not found!')
        return product_id

    class Meta:
        model = Review
        fields = '__all__'