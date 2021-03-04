from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as lgn, authenticate
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "GET" and not request.user.is_authenticated:
        return render(request, 'Accounts/register.html')
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User(first_name=firstname, last_name=lastname, username=username, email=email)
        user.set_password(password1)
        user.save()
        return redirect('/')


def login(request):
    if request.method == 'GET' and not request.user.is_authenticated:
        return render(request, 'Accounts/login.html')
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        i = authenticate(request, username=username, password=password)
        if i:
            lgn(request, i)
            return redirect('/')
        return render(request, 'Accounts/login.html')


@login_required
def logout(request):
    lgt(request)
    return redirect('/')
