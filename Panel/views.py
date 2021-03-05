from django.shortcuts import render, redirect
from Panel.models import Product, Tag
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
        name = request.POST.get('name', '').strip()
        quantity = request.POST.get('quantity', 0).strip()
        price = request.POST.get('price', 0).strip()
        image = request.POST.get('product_image')
        product = Product(name=name, quantity=quantity, price=price, seller=account, image=image)
        product.save()
        tags = [t.strip() for t in request.POST['tag'].split(',')]
        for tag in tags:
            query = Tag.objects.filter(name=tag, product=product)
            if query.count() == 0:
                Tag(name=tag, product=product).save()
        return redirect("/panel/my_products/")

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
                'id': product.pk,
                'tags': product.tag_set.all()
            }
            for product in products
        ]
        return render(request, "Panel/my_products.html", args)


@login_required
def edit_product(request, prd_id):
    product = Product.objects.get(pk=prd_id)
    if request.method == "GET":
        args = {"product": product, 'tags': ','.join([t.name.strip() for t in product.tag_set.all()])}
        return render(request, "Panel/edit_product.html", args)
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.POST.get('product_image')
        tags = [t.strip() for t in request.POST['tag'].split(',')]
        query = Tag.objects.filter(product=product)
        for tag in query:
            tag.delete()
        for tag in tags:
            query = Tag.objects.filter(name=tag, product=product)
            if query.count() == 0:
                Tag(name=tag, product=product).save()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.image = image
        product.save()
        print("*********************************************")
        return redirect("/panel/my_products", )


@login_required
def delete_product(request, prd_id):
    product = Product.objects.get(pk=prd_id)
    Product.objects.get(pk=prd_id).delete()
    return redirect("/panel/my_products", )
