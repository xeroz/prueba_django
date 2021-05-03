from product.models import Category, Cart, User, Product
from product.serializers import (
    CategorySerializer, ProductByCategorySerializer,
    ProductNameByCategorySerializer)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


def get_object(pk):
    try:
        return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404


class CategoryList(APIView):
    """
    List all categories, or create a new cat.
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductByCategoryList(APIView):

    def get(self, request, pk, format=None):
        data = get_object(pk)
        serializer = ProductByCategorySerializer(data)
        return Response(serializer.data)


class ProductNameByCategoryList(APIView):

    def get(self, request, pk, format=None):
        data = get_object(pk)
        serializer = ProductNameByCategorySerializer(data)
        return Response(serializer.data)
