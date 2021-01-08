from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from journaluser.models import BulletJournalUser
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')


def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            data = form.cleaned_data
            print(data)
            user = authenticate(request,
                                username=data["username"], password=data["password"])
            print(user)
            if user:
                login(request, user)
                return redirect("/journal/")
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
            BulletJournalUser.objects.create_user(
                username=data['username'],
                password=data["password1"],
                email=data['email'],
            )
            user = authenticate(
                request, username=data['username'], password=data['password1'])
            print(user)
            if user:
                login(request, user)
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
    return redirect('home')
