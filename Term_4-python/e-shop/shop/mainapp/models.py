import sys
from PIL import Image
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.files.uploadedfile import InMemoryUploadedFile

from io import BytesIO


User = get_user_model()


class MinResolutionErrorException(Exception):
     pass


class MaxResolutionErrorException(Exception):
    pass


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True)
        return products


class LatestProducts:
    objects = LatestProductsManager()

# Create your models here.

# models:
# - Category
# - Product
# - CartProduct
# - Cart
# - Order

# - Customer
# - Specifications (characteristics)


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Category Name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (800, 800)

    # 3 mb
    MAX_IMAGE_SIZE = 314572800000

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Product name')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image')
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # image = self.image
        # img = Image.open(image)
        # min_height, min_width = self.MIN_RESOLUTION
        # max_height, max_width = self.MAX_RESOLUTION
        # if img.height < min_height or img.width < min_width:
        #     raise MinResolutionErrorException('Resolution of image less then min accepted resolution')
        # # print(img.width, img.height)
        # if img.height > max_height or img.width > max_width:
        #     raise MaxResolutionErrorException('Resolution of image more then max accepted resolution')
        # # print(img.width, img.height)
        image = self.image
        img = Image.open(image)
        new_img = img.convert('RGB')
        resized_new_img = new_img.resize((200, 200), Image.ANTIALIAS)
        filestream = BytesIO()
        resized_new_img.save(filestream, 'JPEG', quality=90)
        filestream.seek(0)
        name = '{}.{}'.format(*self.image.name.split('.'))
        self.image = InMemoryUploadedFile(
            filestream, 'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None
        )
        super().save(*args, **kwargs)


class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name='diagonal')
    display = models.CharField(max_length=255, verbose_name='display type')
    processor_freq = models.CharField(max_length=255, verbose_name='Processor Frequency')
    ram = models.CharField(max_length=255, verbose_name='RAM')
    video = models.CharField(max_length=255, verbose_name='Video Card')
    time_without_charge = models.CharField(max_length=255, verbose_name='Battery work time')

    def __str__(self):
        return f'{self.category.name} : {self.title}'


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='diagonal')
    display = models.CharField(max_length= 255, verbose_name='display type')
    resolution = models.CharField(max_length=255, verbose_name='display resolution')
    accum_volume = models.CharField(max_length=255, verbose_name='accum volume')
    ram = models.CharField(max_length=255, verbose_name='RAM')
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name='Max volume of hdd storage')
    main_cap_mp = models.CharField(max_length=255, verbose_name='Main camera')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Front camera')

    def __str__(self):
        return f'{self.category.name} : {self.title}'



# # specific characteristics
# class NotebookProduct(Product):


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')

    # product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Final Price')

    def __str__(self):
        return f'Product: {self.product.title} (for cart)'


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Final Price')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='Address')

    def __str__(self):
        return f'Customer: {self.user.first_name} {self.user.last_name}'


# class Specifiaction(models.Model):
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     name = models.CharField(max_length=255, verbose_name='Name of product for specification')
#
#     def __str__(self):
#         return f'Characteristics for Product: {self.name}'

