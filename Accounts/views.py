from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login as lgn, authenticate
from django.contrib.auth import logout as lgt
from django.contrib.auth.decorators import login_required


# Create your views here.

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
