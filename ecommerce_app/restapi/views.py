from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorator import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import Account
from order.models import Order
from shopping_cart.models import ShoppingCart
from restapi.serializers import AccountSerializer, OrderSerializer, ShoppingCartSerializer
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AccountViewSet(viewsets.ViewSet):
    def get_object(self, request, pk):
        pass

    def list(self, request, format=None):
        pass

    def create(self, request, format=None):
        pass

    def retrieve(self, request, format=None):
        pass

    def update(self, request, pk=None, format=None):
        pass

    def destroy(self, request, pk=None, format=None):
        pass

class ProductListAPIView(APIView):
    permission_classes = []
    parser_classes = []
    renderer_classes = []

    def get_object(self, pk):
        pass

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

class ProductDetailAPIView(APIView):
    permission_classes = []
    parser_classes = []
    renderer_classes = []
    def get_object(self, pk):
        pass

    def get(self, request, pk, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass


class ShoppingCartListAPIView(APIView):
    permission_classes = []
    parser_classes = []
    renderer_classes = []

    def get_object(self, pk):
        pass

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

class ShoppingCartDetailAPIView(APIView):
    permission_classes = []
    parser_classes = []
    renderer_classes = []

    def get_object(self, pk):
        pass

    def get(self, request, pk, format=None):
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass


