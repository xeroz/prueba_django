from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products',)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


# class Orders(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
