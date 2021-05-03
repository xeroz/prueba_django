from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True,
                                max_length=100)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True,
                                 max_length=100)


class ProductByCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True,
                                 max_length=100)
    products = ProductSerializer(many=True, read_only=True)


class ProductNameByCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True,
                                     max_length=100)
    product_order_set = serializers.SerializerMethodField()

    def get_product_order_set(self, instance):
        products = instance.products.all().order_by('name')
        return ProductSerializer(products, many=True, read_only=True).data


class CartByUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True,
                                 max_length=100)
    products = serializers.RelatedField(many=True, read_only=True)
