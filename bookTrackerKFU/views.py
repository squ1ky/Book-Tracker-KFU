from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def index(request):
    return render(request, 'books/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'books/register.html', {"form": form})
