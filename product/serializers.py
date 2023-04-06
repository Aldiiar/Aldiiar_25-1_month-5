from rest_framework import serializers
from product.models import Category, Product, Review
from rest_framework.exceptions import ValidationError


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


class ProductValidateSerializer(serializers.Serializer):
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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150, min_length=3)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    stars = serializers.IntegerField(required=False, min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product not found!')
        return product_id