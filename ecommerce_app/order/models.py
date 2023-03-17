from django.db import models
from account.models import Account
from shopping_cart.models import ShoppingCart

# Create your models here.
class Order(models.Model):
    account = models.ForeignKey(Account, related_name='orders')
    shopping_carts = models.OneToManyField(ShoppingCart, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_add_now=True)
    update = models.DateTimeField(auto_now=True)

    def get_shopping_carts(self):
        return self.shopping_carts
