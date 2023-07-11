from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    data = {
        'products': products,
    }
    return render(request, 'shop/index.html', data)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def profile(request):
    return render(request, 'shop/profile.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def productview(request, product_id):
    product = Product.objects.get(product_id=product_id)
    data = {
        'product': product,
    }
    return render(request, 'shop/productview.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
