from django.contrib import admin
from .models import Product, Suggestions, Order, OrderUpdate
# Register your models here.

admin.site.register(Product)
admin.site.register(Suggestions)
admin.site.register(Order)
admin.site.register(OrderUpdate)
