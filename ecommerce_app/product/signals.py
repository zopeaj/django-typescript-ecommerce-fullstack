from product.models import Product
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=Product)
def calculate_totla_price(sender, instance, action, **kwargs):
    print('action', action)

    total_price = 0
    if action == 'post_add' or action == 'post_remove':
        vat = instance.get_vat()
        price = instance.get_price()
        quantity = instance.get_quantity()
        total_price = price * quantity * vax / 100

    instance.total_price = total_price
    instance.save()
