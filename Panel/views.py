from django.shortcuts import render
from Panel.models import Product


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
