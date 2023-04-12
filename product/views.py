from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product, Review
from product.serializers import ProductsReviewsSerializer, ProductValidateSerializer, \
    CategoryValidateSerializer, ReviewValidateSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryValidateSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class ProductsAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class ReviewsAPIView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class ProductsReviewsAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsReviewsSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET'])
# def products_reviews_api_view(request):
#     products = Product.objects.all()
#     serializer = ProductsReviewsSerializer(products, many=True)
#     return Response(data=serializer.data)




