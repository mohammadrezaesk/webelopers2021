from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.
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
