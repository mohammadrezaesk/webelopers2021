from django.shortcuts import render, redirect
from Panel.models import Product
from Accounts.models import Account


# Create your views here.
def panel(request):
    args = {"error": "", "done": "", "is_seller": False}
    if request.method == "GET" and not request.user.is_authenticated:
        return render(request, 'Accounts/login.html', args)
    account = Account.objects.get(username=request.user.username)
    args['is_seller'] = account.role == 'seller'
    if request.method == "GET":
        return render(request, "Panel/panel.html", args)
    if request.method == "POST":
        if account.role == "buyer":
            account.role = "seller"
            account.save()
            args["done"] = "done"
            args["is_seller"] = True
        else:
            args["error"] = "already_seller_error"

        return render(request, "Panel/panel.html", args)


def create_product(request):
    args = {"error": "", "done": "", "is_seller": False}

    if request.method == "GET" and not request.user.is_authenticated:
        args = {"error": ""}
        return render(request, 'Accounts/login.html', args)
    account = Account.objects.get(username=request.user.username)
    args['is_seller'] = account.role == 'seller'
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product = Product(name=name, quantity=quantity, price=price, seller=account)
        product.save()
    return render(request, "Panel/create_product.html")


def my_products(request):
    args = {"is_seller": False, 'products': []}

    if request.method == "GET" and not request.user.is_authenticated:
        args = {"error": ""}
        return render(request, 'Accounts/login.html', args)
    account = Account.objects.get(username=request.user.username)
    args['is_seller'] = account.role == 'seller'
    if request.method == "GET":
        products = account.product_set.all()
        args["products"] = [
            {
                'class': f'{product.name.replace(" ", "_")}_{product.seller.username.replace(" ", "_")}',
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity
            }
            for product in products
        ]
        return render(request, "Panel/my_products.html", args)
