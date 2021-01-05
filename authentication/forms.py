from django import forms
from django.contrib.auth.forms import UserCreationForm
from journaluser.models import BulletJournalUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = BulletJournalUser
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
