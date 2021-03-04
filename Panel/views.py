from django.shortcuts import render


# Create your views here.
def panel(request):
    return render(request, "Panel/panel.html")


def create_product(request):
    return render(request, "Panel/create_product.html")
