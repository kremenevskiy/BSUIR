from decimal import Decimal
from unittest import mock
from io import BytesIO
import sys

from PIL import Image
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model, authenticate, login
from django.core.files.uploadedfile import SimpleUploadedFile, InMemoryUploadedFile

from .models import Category, CartProduct, Cart, Customer, Notebook, Smartphone
from .utils import recalc_cart
from .views import AddToCartView, BaseView, DeleteFromCartView, RegistrationView

User = get_user_model()
import os

# Create your tests here.


class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Notebooks', slug='notebooks')

        image = SimpleUploadedFile(
            name="notebook_image.jpg",
            content=open('./media/macpro_16.jpeg',"rb").read(),
            content_type="image/jpg")
        self.notebook = Notebook.objects.create(
            category=self.category,
            title="Test Notebook",
            slug="test-slug",
            image=image,
            price=Decimal('2000.00'),
            diagonal="17.3",
            display="IPS",
            processor_freq="3.4 GHz",
            ram="6 GB",
            video="GeForce GTX",
            time_without_charge="18 hours"

        )
        self.customer = Customer.objects.create(user=self.user, phone="1111111", address="Address")
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            content_object=self.notebook
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('2000.00'))

    def test_response_from_add_to_cart_view(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user

        response = AddToCartView.as_view()(request, ct_model="notebook", slug="test-slug")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('mainapp.views.BaseView.get', return_value=mock_data) as mock_data:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code, 444)

    def test_delete_from_cart(self):
        self.client.login(username=self.user.username, password='1234')
        self.cart.products.remove(self.cart_product)
        recalc_cart(self.cart)
        self.assertNotIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 0)

    def test_change_in_cart(self):
        self.client.login(username=self.user.username, password='1234')
        self.cart.products.add(self.cart_product)
        self.cart_product.qty += 1
        self.cart_product.save()
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('4000.00'))

    def test_add_to_cart_not_auth(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('2000.00'))


