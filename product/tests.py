import json
from django.test import TestCase
from .models import Category, Product


class CategoryModelTest(TestCase):

    def setUp(self):
        category = Category.objects.create(name="test_category")
        category2 = Category.objects.create(name="test_category2")

        Product.objects.create(name="test_product", category=category)
        Product.objects.create(name="test_product3", category=category)
        Product.objects.create(name="test_product2", category=category2)

    def test_list_category(self):
        test_data = [
            {"id": 1, "name": "test_category"},
            {"id": 2, "name": "test_category2"}
        ]
        resp = self.client.get("/categories/")
        self.assertEqual(json.dumps(resp.data), json.dumps(test_data))

    def test_product_by_category(self):
        test_data = {
            "id": 1,
            "name": "test_category",
            "products": [
                {"id": 1, "name": "test_product"},
                {"id": 2, "name": "test_product3"}
            ]
        }
        resp = self.client.get("/product-by-category-list/1/")
        self.assertEqual(json.dumps(resp.data), json.dumps(test_data))

    def test_product_name_by_category(self):
        test_data = {
            "id": 1,
            "name": "test_category",
            "product_order_set": [
                {"id": 1, "name": "test_product"},
                {"id": 2, "name": "test_product3"}
            ]
        }
        resp = self.client.get("/product-name-by-category-list/1/")
        self.assertEqual(json.dumps(resp.data), json.dumps(test_data))
