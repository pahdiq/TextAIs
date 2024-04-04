from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def home(request):
    return render(request, 'accounts/home.html')

def start(request):
    return render(request, 'accounts/start.html')

def about(request):
    return render(request, 'accounts/about.html')

def prices(request):
    return render(request, 'accounts/prices.html')