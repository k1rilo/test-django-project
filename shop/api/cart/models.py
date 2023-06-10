from django.db import models
from api.product.models import Product
from accounts.models import UserAccount


class Cart (models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cartsproduct')
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name='cartsuser')
    quantity = models.IntegerField()


    def __str__(self):
        return self.product
    

    def __str__(self):
        return self.quantity

