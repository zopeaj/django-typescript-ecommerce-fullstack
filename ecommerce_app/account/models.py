from django.db import models
from django.contrib.auth.models import User
from order.models import Order

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatar', default=None)
    active = models.BooleanField(default=False)
    order_id = models.ForeignKey(Order, related_name='account')
    orders = models.OneToManyField(Order, on_delete=models.CASCADE)

    def get_orders(self):
        return self.orders
