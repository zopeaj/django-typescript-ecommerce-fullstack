from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.
class ShoppingCart(models.Model):
    shopping_id = models.CharField(default=uuid4().hex, blank=False)
    account = models.ForeignKey(Account, related_name='shopping_cart')
    products = models.OneToManyField(Product, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def get_products(self):
        return self.products

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
