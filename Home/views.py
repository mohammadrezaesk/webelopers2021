from django.shortcuts import render, redirect


# Create your views here.

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
            # TextWithEmail = text + '\n' + email
            # send_mail(title, TextWithEmail, "asdsd@gmail.com", ['webe19lopers@gmail.com'], fail_silently=False, )
        return render(request, 'Home/contact.html', args)
