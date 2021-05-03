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


class CartByUserList(APIView):

    def post(self, request, format=None):
        print(request.data)
        data = request.data
        user = User.objects.get(pk=data.user_id)
        product = Product.objects.get(pk=data.user_id)
        Cart.objects.create(user=user, product=product)
        pass
        # serializer = CategorySerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
