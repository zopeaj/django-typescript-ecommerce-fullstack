from django.urls import path
from account.views import update_account_view, account_home_view, change_password_view, order_list_view,
order_detail_view, shopping_cart_list_view, shopping_cart_detail_view

app_name = 'account'

urlpatterns = [
    path('', account_home_view, name='home'),
    path('update/', update_account_view, name='update'),
    path('change-password/', change_password_view, name='change-password'),
    path('order/', order_list_view, name='order-list'),
    path('order/<int:pk>/', order_detail_view, name='order-detail'),
    path('shopping-cart/', shopping_cart_list_view, name='shopping-cart-list'),
    path('shopping-cart/<int:pk>/', shopping_cart_detail_view, name='shopping-cart-detail'),
]

