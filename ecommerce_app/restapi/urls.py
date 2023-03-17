from rest_framework.routes import DefaultRouter
from django.urls import path
from restapi.views import OrderViewSet, OrderList, OrderDetail, AccountViewSet, ProductListAPIView, ProductDetailAPIView, ShoppingCartListAPIView, ShoppingCartDetailAPIView

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='user')

# account
# account_list = AccountViewSet.as_view({'get': 'list'})
account_detail = AccountViewSet.as_view({'get': 'retreive'})
account_post = AccountViewSet.as_view({'post': 'create'})
account_delete = AccountViewSet.as_view({'delete': 'destroy'})
account_update = AccountViewSet.as_view({'update': 'put'})

# order
order_list = OrderViewSet.as_view({'get':'list'})
order_detail = OrderViewSet.as_view({'get':'retreive'})
order_post = OrderViewSet.as_view({'get': 'create'})
order_update = OrderViewSet.as_view({'update': 'put'})
order_delete = OrderViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('accounts/', include(router.urls)),
    path('accounts/<int:pk>/', account_detail, name='account-detail'),
    path('accounts/<int:pk>/', account_delete, name='account-delete'),
    path('accounts/<int:pk>/', account_update, name='account-update'),

    path('order/', order_post, name='order-add'),
    path('order/all/', order_list, name='order-list'),
    path('order/<int:pk>/', order_detail, name='order-detail'),
    path('order/<int:pk>/', order_update, name='order-update'),
    path('order/<int:pk/', order_delete, name='order-delete'),

    path('shopping-carts/', ShoppingCartListAPIView.as_view(), name='shopping-cart-create-or-list'),
    path('shopping-carts/<int:pk>/', ShoppingCartDetailAPIView.as_view(), name='shopping-cart-detail'),
    path('products/', ProductListAPIView.as_view(), name='product-create-or-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail')
]
