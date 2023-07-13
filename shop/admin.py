from django.contrib import admin
from .models import Product, Suggestions, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Suggestions)
admin.site.register(Order)
