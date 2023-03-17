from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=000)
    category = models.TextField(default='', max_length='60')
    image = models.ImageField(upload_to='product_image', default='None')
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(null=True)
    total_price = models.FloatField(blank=True, null=True)
    vat = modes.FloatField(blank=True)

    def __str__(self):
        return f"Product for the price of {self.price}"

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def get_vat(self):
        return self.vat

class ProductUploadImag(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    product_file = models.FileField(upload_to='product_image', null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.file_name)
