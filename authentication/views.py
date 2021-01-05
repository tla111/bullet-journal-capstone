from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from journaluser.models import BulletJournalUser


def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
    form = LoginForm()
    context = {
        'title': 'SignIn',
        'form': form
    }
    return render(request, 'forms/form.html', context)


def register(request):
    print(request)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            data = form.cleaned_data
            my_user = BulletJournalUser.objects.create(
                username=data['username'],
                password=data["password1"],
                email=data['email'],
            )
            login(request, my_user)
            return redirect("/test/")

    form = RegisterForm()
    context = {
        'title': 'Sign Up for an Account',
        'form': form
    }
    return render(request, 'forms/form.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
