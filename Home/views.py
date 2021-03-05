from django.shortcuts import render, redirect
from django.core.mail import send_mail

from Panel.models import Product, Rate

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
        result_set = Product.objects.all()

    else:
        title = request.POST["title"]
        query = Product.objects.all()
        if request.POST["min_price"]:
            query = query.filter(price__gte=int(request.POST["min_price"]))
        if request.POST["max_price"]:
            query = query.filter(price__lte=int(request.POST["max_price"]))
        if request.POST["title"]:
            query = query.filter(name__contains=request.POST["title"])
        if request.POST["seller_name"]:
            query = query.filter(seller__username__contains=request.POST["seller_name"])
        result_set = query.all()
        print(result_set)
        print(type(result_set))
        if request.POST['tag']:
            result_set = []
            tags = [t.strip() for t in request.POST['tag'].split(',')]
            query = query.all()
            for prd in query:
                if set([t.name for t in prd.tag_set.all()]).intersection(set(tags)):
                    result_set.append(prd)
        # products = Product.objects.filter(, price__lte=max_price, price__gte=min_price).filter().all()

    args['products'] = []
    for product in result_set:
        rates = Rate.objects.filter(product=product).values_list('score', flat=True)
        args["products"].append(
            {
                'class': f'{product.name.replace(" ", "_")}_{product.seller.username.replace(" ", "_")}',
                'name': product.name,
                'price': product.price,
                'pk': product.pk,
                'quantity': product.quantity,
                'seller_first_name': product.seller.first_name,
                'seller_username': product.seller.username,
                'rate': sum(rates) / len(rates) if len(rates) > 0 else 0,
                'seller_last_name': product.seller.last_name,
                'tags': product.tag_set.all()
            })

    return render(request, "Home/all_products.html", args)


def submit_rate(request, prd_id):
    if request.method == "POST":
        rate = request.POST['rate']
        product = Product.objects.get(pk=prd_id)
        Rate(score=int(rate), product=product).save()
    return redirect("/all_products")
