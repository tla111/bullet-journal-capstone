from django import forms
from .models import Assignments, ReflectionPost


class AddAssignment(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)


class AddReflection(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea, required=False)
    name_post = forms.ChoiceField(choices=ReflectionPost.name_choices)

