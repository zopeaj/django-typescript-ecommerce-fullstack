"""ecommerce_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ecommerce_app.views import home_view, login_view, logout_view

app_name = 'ecommerce'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home')
    path('api/v1/', include('restapi.urls'), namespace='restapi'),
    path('account/', include('account.urls', namespace='account')),
    path('product/', include('product.urls', namespace='product')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
