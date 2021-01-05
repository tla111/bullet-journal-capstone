from django import forms
from .models import Assignments

class AddAssignment(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)