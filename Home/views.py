from django.shortcuts import render, redirect
from django.core.mail import send_mail

from Panel.models import Product

from webelopers2021.settings import EMAIL_HOST_USER


def homepage(request):
    if request.method == "GET":
        return render(request, 'Home/homepage.html')


def contactus(request):
    args = {'done': ""}
    if request.method == "GET":
        return render(request, 'Home/contact.html', args)
    else:
        title = request.POST['title']
        email = request.POST['email']
        text = request.POST['text']
        if 10 <= len(text) <= 250:
            args["done"] = "done"
            # contact = ContactUs(title=title, email=email, text=text)
            # contact.save()
            content = email + '\n' + text
            send_mail(title, content, EMAIL_HOST_USER, ['webe21lopers@gmail.com'], fail_silently=False, )
        return render(request, 'Home/contact.html', args)


def all_products(request):
    args = {}
    if request.method == "GET":
        products = Product.objects.all()
    else:
        title = request.POST["title"]
        min_price = int(request.POST["min_price"]) if request.POST["min_price"] else 0
        max_price = int(request.POST["max_price"]) if request.POST["max_price"] else 999999999
        price_query = Product.objects.filter(price__lte=max_price, price__gte=min_price).all()
        name_query = Product.objects.filter(name__contains=title).all()
        products = price_query | name_query
    args["products"] = [
        {
            'class': f'{product.name.replace(" ", "_")}_{product.seller.username.replace(" ", "_")}',
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'seller_first_name': product.seller.first_name,
            'seller_last_name': product.seller.last_name
        }
        for product in products
    ]
    return render(request, "Home/all_products.html", args)
