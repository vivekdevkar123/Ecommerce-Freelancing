from django.db import models
from .choices import PRODUCT_CATEGORY

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50, choices=PRODUCT_CATEGORY, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='shop/images')
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
