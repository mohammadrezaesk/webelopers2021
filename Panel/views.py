from django.shortcuts import render
from Panel.models import Product
from Accounts.models import Account


# Create your views here.
def panel(request):
    return render(request, "Panel/panel.html")


def create_product(request):
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product = Product(name=name, quantity=quantity, price=price)
        product.save()
    return render(request, "Panel/create_product.html")


def become_seller(request):
    args = {"error": "", "done": ""}
    if request.method == "GET":
        return render(request, "Panel/panel.html", args)
    else:
        account = Account.objects.get(username=request.user.username)
        if account.role == "buyer":
            account.role = "seller"
            account.save()
            args["done"] = "done"
        else:
            args["error"] = "already_seller_error"

        return render(request, "Panel/panel.html", args)
