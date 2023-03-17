from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from django.contrib.auth.forms import UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse HttpResponseRedirect
from order.models import Order
from order.forms import OrderCreateForm, OrderUpdateForm
from shopping_cart.models import ShoppingCart
from shopping_cart.forms import ShoppingCartForm
from product.models import Product
# Create your views here.

def update_account_view(request, pk):
    account = Account.objects.get(id=pk)
    update_form = UserUpdateForm()

def account_home_view(request):
    products = Product.objects.all()
    product_search_form = ProductSearchForm(request.POST or None)
    product_data = None
    no_data = None

    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')

        product_qs = Product.objects.filter(name=name, category=category).first()
        if product_qs is not None:
            product_data = product_qs
            single_product_image = product_data.image[0].url
            multiple_product_image = product_data.image.url
        else:
            no_data = f'product {name} not found'


    ctx = {
        'product_form': product_search_form,
        'no_data': no_data,
        'single_product_image': single_product_image,
        'multiple_product_image': multiple_product_image
    }

    return render(request, 'account/home.html', ctx)


@login_required
def change_password_view(request, pk):
    pass


@login_required
def order_detail_view(request, pk):
    pass


@login_required
def order_list_view(request):
    if request.method == 'GET':
        user = User.objects.get_or_create(username=request.user.username)
        account = Account.objects.filter(user=user)
        selected_products_to_order = []
        no_data = None
        orders_from_selected_product = account.get_orders().get_shopping_carts()

        if len(orders_from_selected_product) == 0:
            no_data = 'No order available for purchase'

        for order in orders_from_selected_product:
            if order.selected:
                selected_products_to_order.append(order)

    ctx = {
        'no_data': no_data,
        'selected_products_to_order': selected_products_to_order
    }

    return render(request, 'account/order_list.html', ctx)


@login_required
def shopping_cart_list_view(request):
    pass

@login_required
def shopping_cart_detail_view(request, pk):
    pass

class ShoppingCartListView(LoginRequiredMixin, ListView):
    model = ShoppingCart
    template_name = 'account/shopping_cart_list.html'

class ShoppingCartDetailView(LoginRequiredMixin, DetailView):
    model = ShoppingCart
    template_name = 'account/shopping_cart_detail.html'

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'account/order_list.html'

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'account/order_detail.html'



