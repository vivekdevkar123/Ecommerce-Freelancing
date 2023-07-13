import json
from django.shortcuts import render
from .models import Product, Suggestions, Order
from django.contrib.auth.decorators import login_required


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

        MyMessage = Suggestions(name=name, email=email,
                                phone=phone, desc=desc, user=request.user)
        MyMessage.save()

    return render(request, 'shop/contact.html')


@login_required(login_url='login')
def search(request):
    return render(request, 'shop/search.html')


@login_required(login_url='login')
def profile(request):
    return render(request, 'shop/profile.html')


@login_required(login_url='login')
def tracker(request, order_id):
    order = Order.objects.get(order_id=order_id)
    parsed_orders = []
    item_json = json.loads(order.item_json)
    key_list = list(item_json.keys())
    total_bill = 0
    for i in key_list:
        quantity = item_json[i][0]
        name = item_json[i][1].strip()
        price = item_json[i][2]
        total_bill += int(price) * int(quantity)
        parsed_orders.append([quantity, name, price])

    return render(request, 'shop/tracker.html', {'order': order, 'product': parsed_orders, 'total_bill': total_bill})


def productview(request, product_id):
    product = Product.objects.get(product_id=product_id)
    data = {
        'product': product,
    }
    return render(request, 'shop/productview.html', data)


@login_required(login_url='login')
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
        user = request.user

        order = Order(name=name, email=email, phone=phone, address1=address1,
                      address2=address2, city=city, state=state, zip_code=zip_code, item_json=item_json, user=user)

        order.save()

        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')


@login_required(login_url='login')
def MyOrder(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    parsed_orders = []
    for order in orders:
        item_json = json.loads(order.item_json)
        key_list = list(item_json.keys())
        temp = []
        temp.append(order.order_id)
        temp.append(order.name)
        temp.append(order.order_date)
        for i in key_list:
            quantity = item_json[i][0]
            name = item_json[i][1].strip()
            price = item_json[i][2]
            temp.append([quantity, name, price])

        parsed_orders.append(temp)
    parsed_orders = parsed_orders[::-1]

    return render(request, 'shop/myorder.html', {'orders': parsed_orders})
