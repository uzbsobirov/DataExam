from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

def min_value_validator(value):
    if value < 0:
        raise ValidationError(
            '%(value)s must be greater than or equal to 0',
            params={'value': value},
        )

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Category name'
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True
    )
    description = models.CharField(
        max_length=255,
        verbose_name='category description'
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Category'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ManyToManyField(
        to=Category
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Product name'
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True
    )
    description = models.TextField(
        verbose_name='Product description'
    )
    price = models.DecimalField(
        verbose_name='Product price',
        max_digits=10,
        decimal_places=2,
        validators=[min_value_validator]
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )
    stock_status = models.BooleanField(
        verbose_name='Stock status'
    )
    quantity = models.PositiveBigIntegerField(
        default=0,
        validators=[min_value_validator]
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Invertory'
    
    def save(self, *args, **kwargs):
        return super(Inventory, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name
    
class ProductPhoto(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )
    thumbnail_pc = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )
    large_pc = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ProductPhoto'
    
    def save(self, *args, **kwargs):
        return super(ProductPhoto, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name
    
class Customer(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name='Full name'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Phone number'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Address'
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Customer'
    
    def save(self, *args, **kwargs):
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
    
class Order(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        to=Product
    )
    total_price = models.CharField(
        max_length=255,
        verbose_name='Total price'
    )

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Order'
    
    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.inventory.quantity
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.customer.full_name