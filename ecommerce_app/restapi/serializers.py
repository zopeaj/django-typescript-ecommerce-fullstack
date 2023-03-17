from rest_framework import serializers
from account.models import Account
from shopping_cart.models import ShoppingCart
from order.models import Order
from product.models import Product
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    shopping_cart = ShoppingCartSerializer(many=True)
    order = OrderSerializer(many=True)

    class Meta:
        model = Account
        exclude = ('user', )

    def create(self, validate_data):
        account_data = validate_data.pop('account')
        shopping_cart = validate_data.pop('shopping_cart')
        product_data = []
        order_data = None

        for product in shopping_cart:
            if product.selected:
                product_data.append(product)

        for data in product_data:
            order_data = Order.objects.create(product=data)

        account = Account.objects.create(**account_data, orders=order_data, shopping_cart=shopping_cart)

        return account

    def update(self, instance, validate_data):
        user = validate_data.pop('user')
        user_obj = User.objects.get(username=user.get('username'))
        if user_obj is not None:
            user_obj.username = user.get('username')
            user_obj.password = user.get('password')
            user_obj.email = user.get('email')
        user_obj.save()
        instance.user = user_obj
        instance.created = validate_data.get('created', instance.create)
        instance.updated = validate_data.get('updated', instance.updated)
        instance.avatar = validate_data.get('avatar', instance.avatar)
        instance.rememberme = validate_data.get('rememberme', instance.rememberme)
        instance.save()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('user', )

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('user', )

