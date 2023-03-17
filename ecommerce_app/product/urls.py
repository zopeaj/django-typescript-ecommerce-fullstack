from django.urls import path
from product.views import product_create_view, product_update_view,
product_detail_view, product_delete_view, product_category_list_view,
product_category_detail_view

app_name = 'product'

urlpatterns = [
    path('products/', product_create_view, name='create'),
    path('products/<int:pk>/', product_detail_view, name='detail'),
    # path('products/<int:pk>/', product_delete_view, name='delete'),
    path('products/<ink:pk>/', product_update_view, name='update'),
    path('products/<ink:pk>/category/<str:category>/', product_category_list_view, name='category-list'),
    path('products/<ink:pk>/category/<str:category>/<int:pk>/', product_category_detail_view, name='category-detail'),
]
