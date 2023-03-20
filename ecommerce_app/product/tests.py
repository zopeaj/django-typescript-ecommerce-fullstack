from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

def create_product(name, category, days):
    time = timezone.now() + timedelta(days=days)
    return Product.objects.create(name=name, category=category, created=time)


class ProductIndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)


    def test_index_view(self):
        response = self.client.get(reverse('profiles:home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')
        self.assertEqual(response.context['some_product_list'], SomeObject)
        # <QuerySet [<Product: >]>


class SomeDataIndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_products(self):
        response self.client.get(reverse('product:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No product are available.")
        self.assertQuerysetEqual(response.context['product+_data_list'], [])

    def test_past_products(self):
        product = create_product(name="Milo", category="Beverages", days=-30)
        response = self.client.get(reverse('product:index'))
        self.assertQuerysetEqual(response.context['some_product_list'], [product],)

    def test_future_product(self):
        create_product(name='Suco', category='Beverages', days=30)
        response = self.client.get(reverse('product:index'))
        self.assertContains(response, "No products are available")

    def test_future_products_and_past_product(self):
        product = create_product(name='Iron', category='Electronics', days=30)
        create_product(name='Fridge', category='Electronics', days=-30)
        response = self.client.get(reverse('product:home'))
        self.assertQuerysetEqual(response.context['some_product_list'], [product])


    def test_two_past_questions(self):
        product1 = create_product(name='Hollandia', category='Beverages', days=-30)
        product2 = create_product(name='biro', category='stationeries', days=-5)
        response = self.client.get(reverse('product:home'))
        self.assertQuerysetEqual(response.context['some_product_list'], [product1, product2])


class ProductDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_future_product(self):
        future_product = create_product(name='Slipper', category='wares', days=5)
        url = reverse('product:detail', args=(future_product.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_products(self):
        past_product = create_product(name='Smart Tv', category'Electronics', days=-5)
        url = reverse('product:detail', args=(past_product.id,))
        response = self.client.get(url)
        self.assertContains(response, past_product.name)




