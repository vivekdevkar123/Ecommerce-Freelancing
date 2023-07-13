from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Suggestions, Order, OrderUpdate


def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item["category"] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        allProds.append(list(prod))

    data = {
        'allprods': allProds,
    }
    return render(request, 'shop/index.html', data)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        MyMessage = Suggestions(name=name, email=email, phone=phone, desc=desc)
        MyMessage.save()

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
    return render(request, 'shop/productview.html', data)


def checkout(request):
    if request.method == "POST":
        item_json = request.POST['itemsJson']
        name = request.POST['inputName']
        email = request.POST['inputEmail']
        phone = request.POST['inputPhone']
        address1 = request.POST['inputAddress1']
        address2 = request.POST['inputAddress2']
        city = request.POST['inputCity']
        state = request.POST['inputState']
        zip_code = request.POST['inputZip']

        order = Order(name=name, email=email, phone=phone, address1=address1,
                      address2=address2, city=city, state=state, zip_code=zip_code, item_json=item_json)

        order.save()

        update = OrderUpdate(order_id=order.order_id)
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')
