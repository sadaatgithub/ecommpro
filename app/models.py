from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse("app:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse("app:ProductDetail", args=[self.slug])
    

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='customer_address')
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=50, null=True)
    pincode = models.CharField(max_length=10, null=True)
    contact_no = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.user.first_name

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE, related_name='shipping_Address',null=True)
    first_name  = models.CharField(max_length=100, null=True)
    last_name  = models.CharField(max_length=100, null=True)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=50, null=True)
    pincode = models.CharField(max_length=10, null=True)
    contact_no = models.CharField(max_length=10,null=True)
    email_id = models.EmailField(null=True)

    def __str__(self):
        return self.first_name

class Payment(models.Model):
    # user  = models.ForeignKey(User,on_delete=models.CASCADE, related_name='payer')
    name = models.CharField(max_length=100,null=True)

    
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Payment'

    def __str__(self):
        return self.name