from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from journaluser.models import BulletJournalUser


def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            data = form.cleaned_data
            print(data)
            # username = data["username"]
            # password = data["password"]
            user = authenticate(request,
                                username=data["username"], password=data["password"])
            print(user)
            if user:
                login(request, user)
                return redirect("/profile/")
    form = LoginForm()
    context = {
        'BTN_Text': 'Sign In',
        'title': 'Sign Up!',
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
            my_user = BulletJournalUser.objects.create_user(
                username=data['username'],
                password=data["password1"],
                email=data['email'],
            )
            print(my_user)
            login(request, my_user)
            return redirect("/journal/")

    form = RegisterForm()
    context = {
        'BTN_Text': 'Register',
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'forms/form.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
