from django.db import models
from .choices import PRODUCT_CATEGORY, ORDER_STATUS
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    category = models.CharField(
        max_length=50, choices=PRODUCT_CATEGORY, default="")
    price = models.IntegerField(default=0)
    desc = HTMLField()
    image = models.ImageField(upload_to='shop/images')
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Suggestions(models.Model):
    msg_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    desc = models.CharField(max_length=700)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])

    def __str__(self):
        return self.name
