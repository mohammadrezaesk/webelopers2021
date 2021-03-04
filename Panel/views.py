from django.shortcuts import render, redirect
from Panel.models import Product
from Accounts.models import Account
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def panel(request):
    args = {"error": "", "done": "", "is_seller": False}
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


@login_required
def create_product(request):
    args = {"error": "", "done": "", "is_seller": False}
    account = Account.objects.get(username=request.user.username)
    args['is_seller'] = account.role == 'seller'
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product = Product(name=name, quantity=quantity, price=price, seller=account)
        product.save()
    return render(request, "Panel/create_product.html")


@login_required
def my_products(request):
    args = {"is_seller": False, 'products': []}
    account = Account.objects.get(username=request.user.username)
    args['is_seller'] = account.role == 'seller'
    if request.method == "GET":
        products = account.product_set.all()
        args["products"] = [
            {
                'class': f'{product.name.replace(" ", "_")}_{product.seller.username.replace(" ", "_")}',
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
                'id': product.pk
            }
            for product in products
        ]
        return render(request, "Panel/my_products.html", args)


@login_required
def edit_product(request, prd_id):
    product = Product.objects.get(pk=prd_id)
    if request.method == "GET":
        args = {"product": product}
        return render(request, "Panel/edit_product.html", args)
    else:
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        product.name = name
        product.price = price
        product.quantity = quantity
        product.save()
        print("*********************************************")
        return redirect("/panel/my_products", )


@login_required
def delete_product(request, prd_id):
    product = Product.objects.get(pk=prd_id)
    Product.objects.get(pk=prd_id).delete()
    return redirect("/panel/my_products", )
