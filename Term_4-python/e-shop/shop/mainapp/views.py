from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, View
from django.contrib.auth import authenticate, login

from django.core.mail import send_mail, EmailMessage


from .forms import OrderForm, LoginForm, RegistrationForm
from .mixins import CategoryDetailMixin, CartMixin
from .models import Notebook, Smartphone, Category, LatestProducts, Customer, CartProduct, Order
from .utils import recalc_cart
from threading import Thread
from threading import Event
import sys
sys.path.append("..")
from shop.settings import logging_file, logging_level, EMAIL_HOST_USER
import logging
logging.basicConfig(filename=logging_file, filemode='w', level=getattr(logging, logging_level))


# Create your views here.


class BaseView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_main_page('notebook', 'smartphone', with_respect_to='notebook')
        context = {
            'categories': categories,
            'products': products,
            'cart': self.cart
        }
        return render(request, 'base.html', context)


# def test_view(request):
#     categories = Category.objects.get_categories_for_left_sidebar()
#     return render(request, 'base.html', {'categories': categories})


class ProductDetailView(CartMixin, CategoryDetailMixin, DetailView):

    CT_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    # model = Model
    # queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        context['cart'] = self.cart
        return context


class CategoryDetailView(CartMixin, CategoryDetailMixin, DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context


class AddToCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        if self.cart is None:
            messages.error(request, "For add products should be logged in")
            logging.error("For add products should be logged in")
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner,
            cart=self.cart,
            content_type=content_type,
            object_id=product.id

        )

        if created:
            self.cart.products.add(cart_product)
        # self.cart.save()
        recalc_cart(self.cart)
        # messages.add_message(request, messages.INFO, "Product added successfully")
        return HttpResponseRedirect('/cart/')


class DeleteFromCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner,
            cart=self.cart,
            content_type=content_type,
            object_id=product.id

        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        # self.cart.save()
        recalc_cart(self.cart)
        e = Event()
        t = Thread(target=messages.add_message,
                   args=(request, messages.INFO, "Product removed successfully"))
        t.start()
        t.join(5)
        if t.is_alive():
            logging.warning("thread is not done, setting event to kill thread.")
            e.set()
        else:
            logging.info("thread has already finished.")
        # messages.add_message(request, messages.INFO, "Product removed successfully")
        logging.info("Product deleted successfully")
        return HttpResponseRedirect('/cart/')


class ChangeQTYView(CartMixin, View):
    def post(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner,
            cart=self.cart,
            content_type=content_type,
            object_id=product.id

        )
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        # self.cart.save()
        recalc_cart(self.cart)
        e = Event()
        t = Thread(target=messages.add_message,
                   args=(request, messages.INFO, "Amount changed successfully"))
        t.start()
        t.join(5)
        if t.is_alive():
            logging.warning("thread is not done, setting event to kill thread.")
            e.set()
        else:
            logging.info("thread has already finished.")
        messages.add_message(request, messages.INFO, "Amount changed successfully")
        logging.info("Amount changed successfully")
        return HttpResponseRedirect('/cart/')


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):

        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'cart': self.cart,
            'categories': categories
        }
        return render(request, 'cart.html', context)


class CheckoutView(CartMixin, View):
    def get(self, request, *args, **kwargs):

        categories = Category.objects.get_categories_for_left_sidebar()
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'categories': categories,
            'form': form
        }
        return render(request, 'checkout.html', context)


class MakeOrderView(CartMixin, View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, "Thank you for ordering. Manager will contact you (Or not :)")
            return HttpResponseRedirect('/')
        else:
            customer = Customer.objects.get(user=request.user)
            logging.info("customer is {}".format(customer.user))

            if form.is_valid():
                new_order = form.save(commit=False)
                new_order.customer = customer
                new_order.first_name = form.cleaned_data['first_name']
                new_order.last_name = form.cleaned_data['last_name']
                new_order.phone = form.cleaned_data['phone']
                new_order.address = form.cleaned_data['address']
                new_order.buying_type = form.cleaned_data['buying_type']
                new_order.order_date = form.cleaned_data['order_date']
                new_order.comment = form.cleaned_data['comment']
                new_order.save()
                self.cart.in_order = True
                self.cart.save()
                new_order.cart = self.cart
                new_order.save()
                customer.orders.add(new_order)
                e = Event()
                t = Thread(target=messages.add_message, args=(request, messages.INFO, "Thank you for ordering. Manager will contact you"))
                t.start()
                t.join(5)
                if t.is_alive():
                    logging.warning("thread is not done, setting event to kill thread.")
                    e.set()
                else:
                    logging.info("thread has already finished.")
                # messages.add_message(request, messages.INFO, "Thank you for ordering. Manager will contact you")
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/checkout/')



class LoginView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {'form': form, 'cart': self.cart}
        return render(request, 'login.html', context)


class RegistrationView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart
        }
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']

            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            message = f'''Dear, {user.first_name} {user.last_name} successful registration!'''
            e = Event()
            t = Thread(target=send_mail, args=('eShop registration', message, EMAIL_HOST_USER,
                                               [user.email]), kwargs={'fail_silently': False})
            t.start()
            t.join(10)
            if t.is_alive():
                logging.warning("thread is not done, setting event to kill thread.")
                e.set()
            else:
                logging.info("thread has already finished.")
            return HttpResponseRedirect('/')
        context = {'form': form, 'cart': self.cart}
        return render(request, 'registration.html', context)


class ProfileView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        orders = Order.objects.filter(customer=customer).order_by('-created_at')
        # categories = Category.objects.all()
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'orders': orders,
            'cart': self.cart,
            'categories': categories
        }
        return render(
            request,
            'profile.html',
            context
        )